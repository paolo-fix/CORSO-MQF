"use strict";

const fs = require("fs/promises");
const os = require("os");
const path = require("path");
const crypto = require("crypto");
const vscode = require("vscode");

let writeTimer = undefined;
let outputChannel = undefined;

function getConfig() {
  const config = vscode.workspace.getConfiguration("codexBridge");
  return {
    enabled: config.get("enabled", true),
    writeWorkspaceFile: config.get("writeWorkspaceFile", true),
    writeGlobalFile: config.get("writeGlobalFile", true),
    maxDiagnostics: config.get("maxDiagnostics", 500)
  };
}

function severityName(severity) {
  switch (severity) {
    case vscode.DiagnosticSeverity.Error:
      return "error";
    case vscode.DiagnosticSeverity.Warning:
      return "warning";
    case vscode.DiagnosticSeverity.Information:
      return "information";
    case vscode.DiagnosticSeverity.Hint:
      return "hint";
    default:
      return "unknown";
  }
}

function uriToString(uri) {
  if (!uri) {
    return null;
  }

  if (uri.scheme === "file") {
    return uri.fsPath;
  }

  return uri.toString();
}

function relativeToWorkspace(uri) {
  if (!uri) {
    return null;
  }

  const folder = vscode.workspace.getWorkspaceFolder(uri);
  if (!folder || uri.scheme !== "file") {
    return null;
  }

  return path.relative(folder.uri.fsPath, uri.fsPath);
}

function notebookPathFromCellUri(uri) {
  if (!uri || uri.scheme !== "vscode-notebook-cell") {
    return null;
  }

  try {
    let decodedPath = decodeURIComponent(uri.path);
    if (/^\/[a-zA-Z]:\//.test(decodedPath)) {
      decodedPath = decodedPath.slice(1);
    }
    return decodedPath.replace(/\//g, path.sep);
  } catch (_error) {
    return null;
  }
}

function notebookRelativePathFromCellUri(uri) {
  const notebookPath = notebookPathFromCellUri(uri);
  if (!notebookPath) {
    return null;
  }

  for (const folder of vscode.workspace.workspaceFolders || []) {
    const root = folder.uri.fsPath;
    if (notebookPath.toLowerCase().startsWith(root.toLowerCase())) {
      return path.relative(root, notebookPath);
    }
  }

  return null;
}

function serializeRange(range) {
  return {
    startLine: range.start.line + 1,
    startCharacter: range.start.character + 1,
    endLine: range.end.line + 1,
    endCharacter: range.end.character + 1
  };
}

function serializeDiagnostic(uri, diagnostic) {
  return {
    file: uriToString(uri),
    relativeFile: relativeToWorkspace(uri),
    notebookFile: notebookPathFromCellUri(uri),
    notebookRelativeFile: notebookRelativePathFromCellUri(uri),
    scheme: uri ? uri.scheme : null,
    source: diagnostic.source || null,
    code: diagnostic.code == null ? null : String(diagnostic.code),
    severity: severityName(diagnostic.severity),
    message: diagnostic.message,
    range: serializeRange(diagnostic.range)
  };
}

function collectDiagnostics(maxDiagnostics) {
  const all = [];
  for (const [uri, diagnostics] of vscode.languages.getDiagnostics()) {
    for (const diagnostic of diagnostics) {
      all.push(serializeDiagnostic(uri, diagnostic));
      if (all.length >= maxDiagnostics) {
        return all;
      }
    }
  }
  return all;
}

function serializeTextEditor(editor) {
  if (!editor) {
    return null;
  }

  return {
    file: uriToString(editor.document.uri),
    relativeFile: relativeToWorkspace(editor.document.uri),
    languageId: editor.document.languageId,
    isDirty: editor.document.isDirty,
    isUntitled: editor.document.isUntitled,
    selection: serializeRange(editor.selection)
  };
}

function serializeNotebookEditor(editor) {
  if (!editor) {
    return null;
  }

  const notebook = editor.notebook;
  return {
    file: uriToString(notebook.uri),
    relativeFile: relativeToWorkspace(notebook.uri),
    notebookType: notebook.notebookType,
    isDirty: notebook.isDirty,
    cellCount: notebook.cellCount,
    selections: editor.selections.map((selection) => ({
      start: selection.start,
      end: selection.end
    }))
  };
}

function collectDirtyFiles() {
  const dirty = [];

  for (const document of vscode.workspace.textDocuments) {
    if (document.isDirty) {
      dirty.push({
        type: "text",
        file: uriToString(document.uri),
        relativeFile: relativeToWorkspace(document.uri),
        languageId: document.languageId,
        isUntitled: document.isUntitled
      });
    }
  }

  if (vscode.workspace.notebookDocuments) {
    for (const notebook of vscode.workspace.notebookDocuments) {
      if (notebook.isDirty) {
        dirty.push({
          type: "notebook",
          file: uriToString(notebook.uri),
          relativeFile: relativeToWorkspace(notebook.uri),
          notebookType: notebook.notebookType
        });
      }
    }
  }

  return dirty;
}

function collectWorkspaceFolders() {
  return (vscode.workspace.workspaceFolders || []).map((folder) => ({
    name: folder.name,
    path: folder.uri.fsPath,
    uri: folder.uri.toString()
  }));
}

async function collectGitRepositories() {
  const gitExtension = vscode.extensions.getExtension("vscode.git");
  if (!gitExtension) {
    return [];
  }

  try {
    const git = gitExtension.isActive
      ? gitExtension.exports
      : await gitExtension.activate();
    const api = git.getAPI(1);

    return api.repositories.map((repo) => ({
      rootUri: uriToString(repo.rootUri),
      branch: repo.state.HEAD ? repo.state.HEAD.name : null,
      ahead: repo.state.HEAD && repo.state.HEAD.ahead != null ? repo.state.HEAD.ahead : null,
      behind: repo.state.HEAD && repo.state.HEAD.behind != null ? repo.state.HEAD.behind : null,
      mergeChanges: repo.state.mergeChanges.length,
      indexChanges: repo.state.indexChanges.length,
      workingTreeChanges: repo.state.workingTreeChanges.length,
      untrackedChanges: repo.state.untrackedChanges.length
    }));
  } catch (error) {
    return [{
      error: String(error && error.message ? error.message : error)
    }];
  }
}

function hashWorkspace(workspacePath) {
  return crypto.createHash("sha1").update(workspacePath).digest("hex").slice(0, 12);
}

async function writeJson(filePath, data) {
  await fs.mkdir(path.dirname(filePath), { recursive: true });
  await fs.writeFile(filePath, JSON.stringify(data, null, 2) + "\n", "utf8");
}

async function buildState() {
  const config = getConfig();
  const activeTextEditor = serializeTextEditor(vscode.window.activeTextEditor);
  const activeNotebookEditor = serializeNotebookEditor(vscode.window.activeNotebookEditor);
  const visibleTextEditors = vscode.window.visibleTextEditors.map(serializeTextEditor);
  const visibleNotebookEditors = vscode.window.visibleNotebookEditors
    ? vscode.window.visibleNotebookEditors.map(serializeNotebookEditor)
    : [];
  const workspaceFolders = collectWorkspaceFolders();

  return {
    schemaVersion: 1,
    extensionVersion: "0.1.0",
    generatedAt: new Date().toISOString(),
    machine: os.hostname(),
    workspace: {
      name: vscode.workspace.name || null,
      workspaceFile: vscode.workspace.workspaceFile ? uriToString(vscode.workspace.workspaceFile) : null,
      folders: workspaceFolders
    },
    activeTextEditor,
    activeNotebookEditor,
    visibleTextEditors,
    visibleNotebookEditors,
    dirtyFiles: collectDirtyFiles(),
    diagnostics: collectDiagnostics(config.maxDiagnostics),
    gitRepositories: await collectGitRepositories()
  };
}

async function writeStateNow() {
  const config = getConfig();
  if (!config.enabled) {
    return;
  }

  const state = await buildState();

  if (config.writeGlobalFile) {
    const globalDir = path.join(os.homedir(), ".codex", "vscode-bridge");
    const latestPath = path.join(globalDir, "latest.json");
    await writeJson(latestPath, state);

    const primaryFolder = (vscode.workspace.workspaceFolders || [])[0];
    if (primaryFolder) {
      const workspacePath = primaryFolder.uri.fsPath;
      const workspacePathHash = hashWorkspace(workspacePath);
      await writeJson(path.join(globalDir, "workspaces", `${workspacePathHash}.json`), state);
    }
  }

  if (config.writeWorkspaceFile) {
    for (const folder of vscode.workspace.workspaceFolders || []) {
      await writeJson(path.join(folder.uri.fsPath, ".codex", "vscode_state.json"), state);
    }
  }
}

function scheduleWrite(delayMs = 250) {
  if (writeTimer) {
    clearTimeout(writeTimer);
  }

  writeTimer = setTimeout(async () => {
    writeTimer = undefined;
    try {
      await writeStateNow();
    } catch (error) {
      if (!outputChannel) {
        outputChannel = vscode.window.createOutputChannel("Codex VS Code Bridge");
      }
      outputChannel.appendLine(String(error && error.stack ? error.stack : error));
    }
  }, delayMs);
}

function activate(context) {
  context.subscriptions.push(vscode.commands.registerCommand("codexBridge.writeState", writeStateNow));
  context.subscriptions.push(vscode.window.onDidChangeActiveTextEditor(() => scheduleWrite()));
  context.subscriptions.push(vscode.window.onDidChangeVisibleTextEditors(() => scheduleWrite()));
  context.subscriptions.push(vscode.languages.onDidChangeDiagnostics(() => scheduleWrite(500)));
  context.subscriptions.push(vscode.workspace.onDidSaveTextDocument(() => scheduleWrite()));
  context.subscriptions.push(vscode.workspace.onDidChangeTextDocument(() => scheduleWrite(750)));
  context.subscriptions.push(vscode.workspace.onDidChangeConfiguration((event) => {
    if (event.affectsConfiguration("codexBridge")) {
      scheduleWrite();
    }
  }));

  if (vscode.window.onDidChangeActiveNotebookEditor) {
    context.subscriptions.push(vscode.window.onDidChangeActiveNotebookEditor(() => scheduleWrite()));
  }
  if (vscode.window.onDidChangeVisibleNotebookEditors) {
    context.subscriptions.push(vscode.window.onDidChangeVisibleNotebookEditors(() => scheduleWrite()));
  }
  if (vscode.workspace.onDidChangeNotebookDocument) {
    context.subscriptions.push(vscode.workspace.onDidChangeNotebookDocument(() => scheduleWrite(750)));
  }
  if (vscode.workspace.onDidSaveNotebookDocument) {
    context.subscriptions.push(vscode.workspace.onDidSaveNotebookDocument(() => scheduleWrite()));
  }

  scheduleWrite(1000);
}

function deactivate() {
  if (writeTimer) {
    clearTimeout(writeTimer);
  }
}

module.exports = {
  activate,
  deactivate
};
