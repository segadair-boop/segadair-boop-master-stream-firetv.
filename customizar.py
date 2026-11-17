"""Customize Jellyfin Android TV display name while preserving the upstream GPL-2.0 license."""
from pathlib import Path
import re
import sys

root = Path(sys.argv[1])
assert (root / "app").is_dir(), "Upstream app module missing"
count = 0
for path in (root / "app" / "src").rglob("values/strings.xml"):
    text = path.read_text(encoding="utf-8")
    updated, changed = re.subn(
        r'(<string\s+name="app_name"[^>]*>)(.*?)(</string>)',
        r'\g<1>MASTER STREAM\g<3>',
        text, count=1, flags=re.DOTALL
    )
    if changed:
        path.write_text(updated, encoding="utf-8")
        count += 1
if count == 0:
    raise SystemExit("app_name resource not found: upstream layout requires review")
print(f"MASTER STREAM display name applied to {count} resources")
