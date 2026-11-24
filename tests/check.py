from pathlib import Path

import csv
import os
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def run(*args, code=0):
    script = next(ROOT.glob("*.py"))
    result = subprocess.run(
        [sys.executable, "-B", str(script), *map(str, args)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=dict(os.environ, PYTHONUTF8="1"),
    )
    assert result.returncode == code, result.stderr
    return result.stdout


with tempfile.TemporaryDirectory() as temp:
    base = Path(temp)
    a = base / "names.csv"
    a.write_text("name\nأَحْمَد\n", encoding="utf8")
    target = base / "out.csv"
    run(a, "name", target)
    assert next(
        csv.DictReader(target.read_text(encoding="utf-8-sig").splitlines())
    ) == {"name": "أَحْمَد", "search_key": "احمد"}
