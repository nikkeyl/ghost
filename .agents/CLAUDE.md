# GHOST Claude Code adapter

@AGENTS.md

Use the native Skill tool for matching procedures exposed in
`.claude/skills/`. The portable source is `.agents/skills/active/` in a
checkout; the Claude release contains ordinary skill directories at the
native path. Keep passive detectors outside the native procedure catalog.

If the native catalog is unavailable, report the missing integration
before using direct file reads as a fallback. Do not claim a native
activation or interface badge from a manual read.
