#!/usr/bin/env python3
import re, sys, pathlib, yaml, json
from pathlib import Path

def extract_yaml_blocks(text: str):
    code_fences = re.findall(r"```(?:yaml|yml)?\n(.*?)```", text, flags=re.DOTALL|re.IGNORECASE)
    return code_fences

def main():
    if len(sys.argv) < 3:
        print("usage: extract_yaml.py <input_file> <out_yaml>", file=sys.stderr)
        sys.exit(2)
    inp, outp = Path(sys.argv[1]), Path(sys.argv[2])
    txt = inp.read_text(encoding="utf-8")
    blocks = extract_yaml_blocks(txt)
    if not blocks:
        print("NO_YAML")
        sys.exit(3)
    # take first block
    ytxt = blocks[0].strip()
    outp.write_text(ytxt, encoding="utf-8")
    print("OK")
if __name__ == "__main__":
    main()
