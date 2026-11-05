"""Validate portable skill discovery metadata and root-document local links."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

root = Path(__file__).resolve().parents[1]
errors = []
skills = sorted((root / ".agents/skills").rglob("SKILL.md"))
for path in skills:
    text = path.read_text()
    frontmatter = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.S)
    fields = dict(re.findall(
        r"^(name|description|kind):\s*(.+)$",
        frontmatter[1] if frontmatter else "", re.M
    ))
    for key in ("name", "description", "kind"):
        if not fields.get(key, "").strip().strip("\"'"):
            errors.append(f"{path.relative_to(root)}: missing {key}")
    if fields.get("kind") not in ("active", "passive"):
        errors.append(f"{path.relative_to(root)}: invalid kind")

for name in ("README.md", "AGENTS.md", "CLAUDE.md"):
    path = root / name
    for destination in re.findall(r"\]\(([^)]+)\)", path.read_text()):
        url = urlsplit(destination)
        if url.scheme or url.netloc or not url.path:
            continue
        target = path.parent / unquote(url.path)
        if not target.exists():
            errors.append(f"{name}: missing target {destination}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: metadata for {len(skills)} skills and local links in root documents")
