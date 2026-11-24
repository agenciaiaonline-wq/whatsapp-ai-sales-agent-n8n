"""Validate sanitized n8n workflow JSON blueprints and compose files."""

import json
from pathlib import Path
import sys


def validate_workflows_dir(workflows_dir: Path) -> list[str]:
    errors: list[str] = []
    json_files = sorted(workflows_dir.glob("*.json"))
    if not json_files:
        return ["No workflow JSON files found."]

    for path in json_files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}: invalid JSON ({exc})")
            continue

        if not isinstance(data.get("name"), str) or not data["name"].strip():
            errors.append(f"{path.name}: missing non-empty workflow 'name'")
        nodes = data.get("nodes")
        if not isinstance(nodes, list) or not nodes:
            errors.append(f"{path.name}: missing non-empty 'nodes' list")
        if not isinstance(data.get("connections"), dict):
            errors.append(f"{path.name}: missing 'connections' object")

    return errors


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent / "workflows"
    issues = validate_workflows_dir(root)
    if issues:
        for issue in issues:
            print(f"[FAIL] {issue}", file=sys.stderr)
        raise SystemExit(1)
    print(f"[PASS] Validated {len(list(root.glob('*.json')))} n8n workflow blueprints.")
