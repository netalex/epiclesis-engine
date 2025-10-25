#!/usr/bin/env python3
import sys, yaml, json
from pathlib import Path

SCHEMAS = {
  "ritual": ["id","status","target_epiclesis","goal","anchorage","expected_IE","tm_effect"],
  "artifact": ["id","status","price","limiters"],
  "contract": ["id","status","class","domain","epiclesis_required","anchorage","witnesses","duration","price","limiters","obligations","breach_consequences","lex_stygia"],
  "character": ["id","status","name","tm_profile"],
  "monster": ["id","status","class","treatment"]
}

def validate_yaml(path: Path, expect: str):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    ok = True; missing = []
    if expect in SCHEMAS:
        req = SCHEMAS[expect]
        for key in req:
            if key not in data:
                ok = False; missing.append(key)
        # soft checks
        if "id" in data and ":" not in data["id"]:
            ok = False; missing.append("id (must include prefix, e.g., ritual:..., artifact:...)")
    return ok, missing

def main():
    if len(sys.argv) < 3:
        print("usage: validate_yaml.py <yaml_file> <expect:{ritual|artifact|contract|character|monster|any}>", file=sys.stderr)
        sys.exit(2)
    yfile = Path(sys.argv[1])
    expect = sys.argv[2]
    try:
        if expect == "any":
            yaml.safe_load(yfile.read_text(encoding="utf-8"))
            print(json.dumps({"valid":True,"missing":[]}))
            sys.exit(0)
        ok, missing = validate_yaml(yfile, expect)
        print(json.dumps({"valid":ok,"missing":missing}))
        sys.exit(0 if ok else 4)
    except Exception as e:
        print(json.dumps({"valid":False,"error":str(e)}))
        sys.exit(4)

if __name__ == "__main__":
    main()
