"""Package repository Markdown and its license, preserving discovery paths."""

import argparse
import hashlib
from pathlib import Path
import re
import subprocess
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("version", nargs="?", default="snapshot")
args = parser.parse_args()
if not re.fullmatch(r"snapshot|v\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", args.version):
    parser.error("version must be snapshot or a tag such as v1.0.0")

paths = subprocess.check_output(
    ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
    cwd=root,
).decode().split("\0")
files = sorted(
    {p for p in paths if Path(p).suffix.lower() == ".md" or p == "LICENSE"}
)
if "AGENTS.md" not in files or "LICENSE" not in files:
    raise SystemExit("AGENTS.md and LICENSE are required")
for name in files:
    path = root / name
    if path.is_symlink() or not path.is_file():
        raise SystemExit(f"Not a regular release file: {name}")

output = root / "dist"
output.mkdir(exist_ok=True)
archive = output / f"ghost-{args.version}.zip"
with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
    for name in files:
        entry = ZipInfo(f"ghost-{args.version}/{name}")
        entry.compress_type = ZIP_DEFLATED
        entry.external_attr = 0o100644 << 16
        bundle.writestr(entry, (root / name).read_bytes())
checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
(output / "SHA256SUMS").write_text(f"{checksum}  {archive.name}\n")
print(f"Created {archive.name}: {len(files)} files, SHA-256 {checksum}")
