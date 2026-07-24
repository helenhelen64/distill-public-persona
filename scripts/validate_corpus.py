#!/usr/bin/env python3
"""Validate a public-persona corpus in JSONL or CSV format."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


REQUIRED = ("id", "text", "created_at", "source_type")
ALLOWED_TYPES = {
    "original",
    "reply",
    "quote",
    "repost",
    "profile",
    "article",
    "transcript",
    "other",
}


def records(path: Path) -> Iterable[tuple[int, dict[str, Any]]]:
    if path.suffix.lower() == ".jsonl":
        with path.open(encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                if line.strip():
                    yield line_number, json.loads(line)
        return

    if path.suffix.lower() == ".csv":
        with path.open(encoding="utf-8-sig", newline="") as handle:
            for line_number, row in enumerate(csv.DictReader(handle), 2):
                yield line_number, dict(row)
        return

    raise ValueError("Supported formats: .jsonl and .csv")


def parse_date(value: str) -> bool:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def validate(path: Path) -> tuple[dict[str, Any], list[str]]:
    errors: list[str] = []
    ids: set[str] = set()
    source_types: Counter[str] = Counter()
    languages: Counter[str] = Counter()
    dates: list[str] = []
    count = 0

    try:
        iterator = records(path)
        for line_number, row in iterator:
            count += 1
            if not isinstance(row, dict):
                errors.append(f"line {line_number}: record must be an object")
                continue

            missing = [field for field in REQUIRED if not str(row.get(field, "")).strip()]
            if missing:
                errors.append(f"line {line_number}: missing {', '.join(missing)}")

            record_id = str(row.get("id", "")).strip()
            if record_id:
                if record_id in ids:
                    errors.append(f"line {line_number}: duplicate id {record_id}")
                ids.add(record_id)

            source_type = str(row.get("source_type", "")).strip()
            if source_type:
                source_types[source_type] += 1
                if source_type not in ALLOWED_TYPES:
                    errors.append(f"line {line_number}: unknown source_type {source_type}")

            created_at = str(row.get("created_at", "")).strip()
            if created_at:
                if parse_date(created_at):
                    dates.append(created_at)
                else:
                    errors.append(f"line {line_number}: invalid ISO date {created_at}")

            language = str(row.get("language", "")).strip()
            if language:
                languages[language] += 1
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors.append(str(exc))

    report = {
        "path": str(path),
        "records": count,
        "unique_ids": len(ids),
        "source_types": dict(source_types),
        "languages": dict(languages),
        "earliest_created_at": min(dates) if dates else None,
        "latest_created_at": max(dates) if dates else None,
        "error_count": len(errors),
        "status": "valid" if not errors and count else "invalid",
    }
    if count == 0:
        errors.append("corpus contains no records")
        report["error_count"] = len(errors)
    return report, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("corpus", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    report, errors = validate(args.corpus)
    payload = json.dumps({"summary": report, "errors": errors}, ensure_ascii=False, indent=2)
    print(payload)
    if args.report:
        args.report.write_text(payload + "\n", encoding="utf-8")
    return 0 if report["status"] == "valid" else 1


if __name__ == "__main__":
    sys.exit(main())
