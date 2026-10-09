#!/usr/bin/env bash
# Install (or re-sync) the feynman-technique skill.
#
#   ./install.sh                 # personal, Claude Code  (~/.claude/skills)
#   ./install.sh --project       # this repo             (.claude/skills)
#   ./install.sh --all           # every tool dir found on this machine
#   ./install.sh --to <dir>      # somewhere specific
#   ./install.sh --check         # report drift, change nothing
#
# Safe to run repeatedly: it replaces the installed copy with this one.

set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/skills/feynman-technique"
NAME="feynman-technique"

[ -f "$SRC/SKILL.md" ] || { echo "error: $SRC/SKILL.md not found" >&2; exit 1; }

# Where the tools look. ~/.agents is the emerging cross-tool convention.
CANDIDATES=(
  "$HOME/.claude/skills"    # Claude Code
  "$HOME/.agents/skills"    # Codex CLI, and read by several others
  "$HOME/.cursor/skills"    # Cursor
  "$HOME/.copilot/skills"   # VS Code / GitHub Copilot
  "$HOME/.gemini/skills"    # Gemini CLI
)

install_to() {
  local dest="$1"
  mkdir -p "$dest"
  rm -rf "${dest:?}/$NAME"
  cp -R "$SRC" "$dest/"
  echo "  installed  ${dest/#$HOME/~}/$NAME"
}

case "${1:-}" in
  --check)
    status=0
    for dir in "${CANDIDATES[@]}"; do
      [ -d "$dir/$NAME" ] || continue
      if diff -rq "$SRC" "$dir/$NAME" >/dev/null 2>&1; then
        echo "  up to date  ${dir/#$HOME/~}/$NAME"
      else
        echo "  STALE       ${dir/#$HOME/~}/$NAME"
        status=1
      fi
    done
    [ $status -eq 0 ] || echo $'\nRun ./install.sh --all to re-sync.'
    exit $status
    ;;
  --all)
    found=0
    for dir in "${CANDIDATES[@]}"; do
      # only refresh tools that already exist, plus Claude Code by default
      if [ -d "$dir" ] || [ "$dir" = "$HOME/.claude/skills" ]; then
        install_to "$dir"; found=1
      fi
    done
    [ $found -eq 1 ] || echo "  no known skill directories found"
    ;;
  --project)
    install_to "$(pwd)/.claude/skills"
    echo "  commit it and your team gets it too"
    ;;
  --to)
    [ -n "${2:-}" ] || { echo "error: --to needs a directory" >&2; exit 1; }
    install_to "$2"
    ;;
  "")
    install_to "$HOME/.claude/skills"
    ;;
  *)
    sed -n '2,12p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
    exit 1
    ;;
esac

echo
echo "Restart your agent, then try:  /feynman-technique what is a hash function?"
