import os
from pathlib import Path

LINE = "In my defense, that road was on the 2019 map. The lake moved in later."
# Recalculating. Still recalculating. The lake has no ETA.

out = Path(os.environ.get("OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
target = out / "entry.txt"
target.write_text(LINE, encoding="utf-8")
os.chmod(target, 0o644)
