#!/usr/bin/env python3
import csv, json, re, sys
from pathlib import Path

def infer_provider(p: Path):
    # expect path: .../out/golden/<provider>/<file>
    try:
        return p.parent.name
    except Exception:
        return "unknown"

def infer_model_from_text(text: str):
    # heuristic placeholder (user can edit later)
    return ""

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="dir outputs")
    ap.add_argument("--csv", required=True, help="results csv path")
    args = ap.parse_args()

    outdir = Path(args.out)
    rows = []
    for of in sorted(outdir.glob("*/*.out.md")):
        provider = infer_provider(of)
        stem = of.name.split(".")[0]  # e.g., 02_rito_yaml_from_brief.20251025-101010.out.md
        golden_id = stem.split(".")[0]
        text = of.read_text(encoding="utf-8", errors="ignore")
        # default flags
        yaml_found = "```" in text and ("yaml" in text.lower() or "---" in text[:200])
        yaml_valid = ""
        status = ""
        # set expectations by golden id prefix
        expect = None
        if golden_id.startswith("02_"):
            expect="ritual"
        elif golden_id.startswith("04_"):
            expect="contract"
        elif golden_id.startswith("08_"):
            expect="artifact"

        if expect:
            # try to find sibling yaml file with same timestamp
            ypath = of.with_suffix("").with_suffix(".yaml")  # naive mapping
            if ypath.exists():
                yaml_found = True
                try:
                    import yaml as _yaml
                    data = _yaml.safe_load(ypath.read_text(encoding="utf-8"))
                    # minimal validation
                    req = {
                        "ritual": ["id","status","target_epiclesis","goal","anchorage","expected_IE","tm_effect"],
                        "artifact": ["id","status","price","limiters"],
                        "contract": ["id","status","class","domain","epiclesis_required","anchorage","witnesses","duration","price","limiters","obligations","breach_consequences","lex_stygia"]
                    }[expect]
                    missing = [k for k in req if k not in data]
                    yaml_valid = "yes" if not missing else f"no(missing:{','.join(missing)})"
                except Exception as e:
                    yaml_valid = f"no(error:{e})"
            else:
                yaml_valid = "no(file_missing)"
            status = "pass" if yaml_valid.startswith("yes") else "fail"
        else:
            status = "n/a"

        rows.append([
            str(of.stat().st_mtime_ns), provider, infer_model_from_text(text), golden_id, str(of), 
            "yes" if yaml_found else "no", yaml_valid, status, ""
        ])

    # write/append
    csvpath = Path(args.csv)
    write_header = not csvpath.exists()
    with open(csvpath, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow(["date","provider","model","golden_id","output_file","yaml_found","yaml_valid","status","notes"])
        for r in rows:
            w.writerow(r)
    print(f"Appended {len(rows)} rows to {csvpath}")
if __name__ == "__main__":
    main()
