#!/usr/bin/env python3
"""Generate one Markdown summary table from benchmark_results.json.

Usage:
    python benchmark_report_table.py benchmark_results.json

If the path is omitted, benchmark_results.json in the current directory is used.
The only output file is benchmark_report_table.md, next to the JSON input.
No external dependencies are required.
"""

import json
import sys
from pathlib import Path


HEADERS = ["Dataset", "Algorithm", "Success", "Success rate", "Mean conflicts", "Mean time (s)"]


def build_table(datasets):
    """Extract the key results from the benchmark JSON."""
    rows = []
    for dataset in datasets:
        name = dataset["dataset"].removeprefix("data_").removesuffix(".json").replace("_", " ")
        for algorithm, result in dataset["results"].items():
            runs = int(result["runs"])
            success = int(result["success"])
            mean_conflicts = float(result["mean_conflicts"])
            mean_time = float(result["mean_time_seconds"])

            # 999 is a failure marker for DFS, NOT a real conflict count.
            conflicts_text = (
                "N/A"
                if algorithm == "DFS + Backtracking" and mean_conflicts == 999
                else f"{mean_conflicts:.2f}"
            )
            rows.append([
                name,
                algorithm,
                f"{success}/{runs}",
                f"{100 * success / runs:.0f}%" if runs else "N/A",
                conflicts_text,
                f"{mean_time:.2f}",
            ])
    return rows


def to_markdown(rows):
    lines = [
        "# Timetabling benchmark — key results",
        "",
        "| " + " | ".join(HEADERS) + " |",
        "| " + " | ".join("---" for _ in HEADERS) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in rows)
    lines.extend([
        "",
        "*Mean time includes all runs, including unsuccessful ones. "
        "N/A means no complete timetable was returned; 999 is a failure marker, "
        "not a measured conflict count.*",
        "",
    ])
    return "\n".join(lines)


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python benchmark_report_table.py [benchmark_results.json]")

    source = Path(sys.argv[1]) if len(sys.argv) == 2 else Path("benchmark_results.json")
    if source.suffix.lower() != ".json":
        sys.exit("Error: the input must be a .json file.")
    if not source.is_file():
        sys.exit(f"File not found: {source}")

    with source.open(encoding="utf-8") as handle:
        datasets = json.load(handle)

    output = source.with_name("benchmark_report_table.md")
    output.write_text(to_markdown(build_table(datasets)), encoding="utf-8")
    print(f"Markdown table created: {output}")


if __name__ == "__main__":
    main()
