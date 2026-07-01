# Codex VS Code Bridge

Local VS Code extension that exports editor state to JSON for Codex sessions.

It writes:

- workspace folders;
- active text editor and active notebook editor;
- visible editors;
- dirty files;
- Problems panel diagnostics;
- basic Git repository status.

Output paths:

- `<workspace>/.codex/vscode_state.json`
- `%USERPROFILE%/.codex/vscode-bridge/latest.json`

The extension has no external dependencies.
