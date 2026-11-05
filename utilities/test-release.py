"""Exercise archive completeness, ignored files, paths, and reproducibility."""

import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from zipfile import ZipFile

builder = Path(__file__).with_name("build-release.py")
with tempfile.TemporaryDirectory(prefix="ghost-release-") as directory:
    root = Path(directory)
    (root / "utilities").mkdir()
    shutil.copyfile(builder, root / "utilities/build-release.py")
    subprocess.run(["git", "init", "-q", directory], check=True)
    content = {
        "AGENTS.md": b"# GHOST\n",
        "LICENSE": b"MIT\n",
        "docs/space in name.md": "# 日本語\n".encode(),
        ".agents/skills/example/SKILL.md": b"# Example\n",
        "UPPER.MD": b"# Uppercase extension\n",
        "node_modules/vendor/README.md": b"Excluded\n",
        ".gitignore": b"node_modules/\ndist/\n",
        "package.json": b"{}\n",
    }
    for name, data in content.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    # Include tracked files and a newly authored, untracked document.
    subprocess.run(
        ["git", "-c", "core.autocrlf=false", "add", "."], cwd=root, check=True
    )
    content["docs/new.md"] = b"# New\n"
    (root / "docs/new.md").write_bytes(content["docs/new.md"])
    command = [sys.executable, "utilities/build-release.py", "v1.2.3"]
    subprocess.run(command, cwd=root, check=True, capture_output=True)
    archive = root / "dist/ghost-v1.2.3.zip"
    archive_bytes = archive.read_bytes()
    expected = {
        f"ghost-v1.2.3/{name}": data
        for name, data in content.items()
        if (name.endswith((".md", ".MD")) or name == "LICENSE")
        and not name.startswith("node_modules/")
    }
    with ZipFile(archive) as bundle:
        assert {n: bundle.read(n) for n in bundle.namelist()} == expected
    assert (root / "dist/SHA256SUMS").read_text() == (
        f"{hashlib.sha256(archive_bytes).hexdigest()}  {archive.name}\n"
    )
    subprocess.run(command, cwd=root, check=True, capture_output=True)
    assert archive.read_bytes() == archive_bytes
    result = subprocess.run(
        command[:-1] + ["../../outside"], cwd=root, capture_output=True
    )
    assert result.returncode != 0
    (root / "docs/new.md").unlink()
    (root / "docs/new.md").symlink_to(root / "LICENSE")
    result = subprocess.run(command, cwd=root, capture_output=True)
    assert result.returncode != 0
print("PASS: contents, hidden paths, checksum, repeatability, invalid inputs")
