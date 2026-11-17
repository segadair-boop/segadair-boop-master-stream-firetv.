"""Rename the upstream Jellyfin Android TV application labels for MASTER STREAM."""
from pathlib import Path
import re
import sys

root = Path(sys.argv[1])
path = root / "app" / "src" / "main" / "res" / "values" / "strings.xml"
if not path.exists():
    raise SystemExit(f"Required Android strings missing: {path}")
original = path.read_text(encoding="utf-8")
modified = original
for key in ("app_name_release", "app_name_debug"):
    pattern = rf'(<string\s+name="{key}"[^>]*>)(.*?)(</string>)'
    replacement = "MASTER STREAM" if key == "app_name_release" else "MASTER STREAM (Teste)"
    modified, count = re.subn(pattern, lambda m: m.group(1) + replacement + m.group(3), modified, count=1, flags=re.DOTALL)
    if count != 1:
        raise SystemExit(f"Missing resource: {key}")
path.write_text(modified, encoding="utf-8")
print("MASTER STREAM labels updated")
