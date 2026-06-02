#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

if [[ ! -f .venv/bin/activate ]]; then
    echo "Virtual environment not found. Run scripts/setup.sh first." >&2
    exit 1
fi

# shellcheck disable=SC1091
source .venv/bin/activate
cd src
python main.py
