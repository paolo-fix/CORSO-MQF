"""Raccoglie evidenze per l'aggiornamento di MQF_Stato_Avanzamento.md.

Lo script non assegna stati e non modifica documenti: rende verificabile il
materiale su cui l'agente editoriale deve basare la valutazione.

Uso:
    conda run -n quick_env python tools/audit_stato_avanzamento.py
    conda run -n quick_env python tools/audit_stato_avanzamento.py --since 2026-09-01
"""

from __future__ import annotations

import argparse
import re
import subprocess
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "00_MasterPlan" / "MQF_Stato_Avanzamento.md"
SNAPSHOT_RE = re.compile(r"^## Snapshot al (\d{4}-\d{2}-\d{2})", re.MULTILINE)
LESSON_RE = re.compile(r"(?:Lez(?:ione)?[_ -]?|Cap[_ -]?)(\d{1,2})", re.IGNORECASE)
SECTION_RE = re.compile(r"^\\(?:chapter|section|subsection|subsubsection)\{(.+?)\}", re.MULTILINE)
FRAME_RE = re.compile(r"\\begin\{frame\}")
EXERCISE_RE = re.compile(r"\\begin\{exercise\}")
FIGURE_RE = re.compile(r"\\includegraphics")


def run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=True,
        capture_output=True,
    )
    return result.stdout


def snapshot_date() -> str:
    match = SNAPSHOT_RE.search(STATUS_PATH.read_text(encoding="utf-8"))
    if not match:
        raise RuntimeError(f"Snapshot non trovato in {STATUS_PATH.relative_to(ROOT)}")
    return match.group(1)


def lesson_numbers(path: str) -> set[int]:
    return {int(value) for value in LESSON_RE.findall(path)}


def tex_summary(path: Path, kind: str) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    sections = SECTION_RE.findall(text)
    heading = "; ".join(sections[:8]) or "nessuna sezione rilevata"
    if len(sections) > 8:
        heading += "; ..."
    if kind == "manuale":
        return (
            f"{path.relative_to(ROOT)} — {len(sections)} sezioni, "
            f"{len(EXERCISE_RE.findall(text))} esercizi, "
            f"{len(FIGURE_RE.findall(text))} figure. Sezioni: {heading}"
        )
    return (
        f"{path.relative_to(ROOT)} — {len(FRAME_RE.findall(text))} frame, "
        f"{len(FIGURE_RE.findall(text))} figure. Sezioni: {heading}"
    )


def lesson_artifacts(lesson: int) -> list[str]:
    token = f"{lesson:02d}"
    candidates = [
        (ROOT / "01_Manuale" / "Capitoli", "manuale"),
        (ROOT / "02_Slides", "slides"),
        (ROOT / "04_Codice", "codice"),
        (ROOT / "05_CodiceSt", "codice"),
        (ROOT / "graphics", "grafici"),
    ]
    found: list[str] = []
    matcher = re.compile(rf"(?:Lez|Cap)[_-]?{token}(?!\d)", re.IGNORECASE)
    for directory, kind in candidates:
        if not directory.exists():
            continue
        for path in sorted(p for p in directory.rglob("*") if p.is_file()):
            if not matcher.search(path.name) and not matcher.search(str(path.parent)):
                continue
            if path.suffix.lower() == ".tex":
                found.append(tex_summary(path, "manuale" if kind == "manuale" else "slides"))
            else:
                found.append(f"{path.relative_to(ROOT)} — {kind}")
    return found


def changed_paths(since: str) -> list[str]:
    output = run_git("log", f"--since={since}", "--name-only", "--format=")
    return sorted({line.strip() for line in output.splitlines() if line.strip()})


def worktree_paths(status: str) -> list[str]:
    paths: list[str] = []
    for line in status.splitlines():
        if len(line) < 4:
            continue
        # Il formato porcelain ha due colonne di stato; il separatore può
        # apparire una o due volte nella resa della shell, quindi si rimuovono
        # soltanto le due colonne e gli spazi successivi.
        path = line[2:].strip()
        if " -> " in path:
            path = path.rsplit(" -> ", 1)[1]
        paths.append(path.strip('"'))
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--since",
        help="Data iniziale YYYY-MM-DD; per default legge lo snapshot nello stato.",
    )
    args = parser.parse_args()
    since = args.since or snapshot_date()

    changed = changed_paths(since)
    worktree = run_git("status", "--short").strip()
    lessons: dict[int, list[tuple[str, str]]] = defaultdict(list)
    transversal: list[str] = []
    for source, paths in (("Git", changed), ("worktree", worktree_paths(worktree))):
        for path in paths:
            numbers = lesson_numbers(path)
            if numbers:
                for lesson in numbers:
                    lessons[lesson].append((source, path))
            elif path not in transversal:
                transversal.append(path)

    print(f"# Audit Stato di Avanzamento dal {since}")
    print()
    print("## Modifiche locali non registrate")
    print(worktree if worktree else "Nessuna.")
    print()
    print("## Lezioni con evidenze nuove")
    if not lessons:
        print("Nessuna lezione individuata dai nomi dei file modificati.")
    for lesson in sorted(lessons):
        print(f"### Lezione {lesson}")
        print("Modifiche Git:")
        for source, path in lessons[lesson]:
            print(f"- [{source}] `{path}`")
        print("Materiali presenti:")
        artifacts = lesson_artifacts(lesson)
        if artifacts:
            for artifact in artifacts:
                print(f"- {artifact}")
        else:
            print("- Nessun materiale con convenzione LezNN/CapNN rilevato.")
        print()

    print("## Modifiche trasversali")
    if transversal:
        for path in transversal:
            print(f"- `{path}`")
    else:
        print("Nessuna.")


if __name__ == "__main__":
    main()
