#!/usr/bin/env python3
"""Render report diagrams in temporary export files; preserve Markdown sources."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("source", type=Path)
parser.add_argument("build_dir", type=Path)
args = parser.parse_args()
original = args.source.read_bytes()
text = original.decode("utf-8")
opening = re.findall(r"(?m)^```mermaid\s*$", text)
blocks = re.findall(r"(?ms)^```mermaid\s*\n(.*?)^```\s*$", text)
if len(opening) != len(blocks):
    raise SystemExit("Unbalanced Mermaid fence in export source")
output = args.build_dir / "mermaid-rendered.md"
if not blocks:
    output.write_bytes(original)
else:
    cli = os.environ.get("NEXA_MERMAID_CLI") or shutil.which("mmdc")
    if not cli:
        raise SystemExit("Install @mermaid-js/mermaid-cli@12.0.0 or set NEXA_MERMAID_CLI")
    version = subprocess.check_output([cli, "--version"], text=True).strip()
    if version != "12.0.0":
        raise SystemExit("Report export requires mermaid-cli 12.0.0")
    command = [cli, "-i", str(args.source), "-o", str(output), "-e", "png",
               "-j", "2", "-s", "2", "-b", "white"]
    browser = os.environ.get("NEXA_MERMAID_BROWSER")
    default_browser = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
    if not browser and default_browser.is_file():
        browser = str(default_browser)
    if browser:
        config = args.build_dir / "mermaid-browser.json"
        config.write_text(json.dumps({"executablePath": browser}))
        command += ["-p", str(config)]
    subprocess.run(command, check=True)
    figures = list(args.build_dir.glob("mermaid-rendered-*.png"))
    if len(figures) != len(blocks) or not all(p.stat().st_size for p in figures):
        raise SystemExit("Rendered diagram count does not match source")
    if "```mermaid" in output.read_text():
        raise SystemExit("Unrendered Mermaid block remains")
if hashlib.sha256(args.source.read_bytes()).digest() != hashlib.sha256(original).digest():
    raise SystemExit("Export source was unexpectedly modified")
print(f"Rendered {len(blocks)} Mermaid diagrams")
