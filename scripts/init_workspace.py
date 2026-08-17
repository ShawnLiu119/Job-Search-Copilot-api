#!/usr/bin/env python3
"""Initialize a local, resumable workspace for job-search-copilot."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--resume", required=True, type=Path)
    parser.add_argument("--keyword", action="append", default=[])
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    resume = args.resume.expanduser().resolve()
    if not resume.is_file():
        raise SystemExit(f"Resume not found: {resume}")
    if resume.suffix.lower() not in {".pdf", ".docx"}:
        raise SystemExit("Resume must be a PDF or DOCX file")

    root = args.root.expanduser().resolve()
    for directory in (
        root / "source",
        root / "job-descriptions",
        root / "tailored-resumes",
        root / "outreach",
        root / "runs",
    ):
        directory.mkdir(parents=True, exist_ok=True)

    target = root / "source" / f"master-resume{resume.suffix.lower()}"
    incoming_hash = sha256(resume)
    if target.exists() and sha256(target) != incoming_hash:
        raise SystemExit(
            f"A different master resume already exists at {target}; preserve it or choose a new workspace"
        )
    if not target.exists():
        shutil.copy2(resume, target)

    for ledger_name in ("jobs.jsonl", "contacts.jsonl"):
        (root / ledger_name).touch(exist_ok=True)

    config_path = root / "config.json"
    now = utc_now()
    normalized_keywords = list(dict.fromkeys(k.strip() for k in args.keyword if k.strip()))
    if config_path.exists():
        config = json.loads(config_path.read_text(encoding="utf-8"))
        existing = config.get("keywords", [])
        config["keywords"] = list(dict.fromkeys([*existing, *normalized_keywords]))
        preferences = config.setdefault("preferences", {})
        preferences.setdefault("locations", [])
        preferences.setdefault("work_arrangements", [])
        preferences.setdefault("relocation_willingness", "unknown")
        preferences.setdefault("preferences_confirmed_at", None)
        preferences.setdefault("industries", [])
        preferences.setdefault("seniority", [])
        preferences.setdefault("salary", None)
        preferences.setdefault("work_authorization", "unknown")
        preferences.setdefault("sponsorship_required", "unknown")
        config["updated_at"] = now
    else:
        config = {
            "schema_version": 1,
            "resume": {
                "path": str(target.relative_to(root)),
                "sha256": incoming_hash,
            },
            "keywords": normalized_keywords,
            "inferred_role_families": [],
            "preferences": {
                "locations": [],
                "work_arrangements": [],
                "relocation_willingness": "unknown",
                "preferences_confirmed_at": None,
                "industries": [],
                "seniority": [],
                "salary": None,
                "work_authorization": "unknown",
                "sponsorship_required": "unknown",
            },
            "exclusions": [],
            "created_at": now,
            "updated_at": now,
        }
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"workspace": str(root), "config": str(config_path)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
