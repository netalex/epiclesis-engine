#!/usr/bin/env python3
import argparse, sys, json, yaml, pathlib
from jsonschema import validate, Draft202012Validator, exceptions as jsex

SCHEMA_PATH = pathlib.Path(__file__).resolve().parents[1] / "ontology" / "core_schema.json"

def load(p):
    with open(p, "r", encoding="utf-8") as f:
        if p.endswith(".json"):
            return json.load(f)
        return yaml.safe_load(f)

def guess_type(obj):
    # inspect minimal keys to suggest which def to validate against
    if "domains" in obj and "epicleses" in obj: return "Deity"
    if "target_epiclesis" in obj: return "Ritual"
    if "verb" in obj and "patron" in obj: return "Artifact"
    if "rule" in obj and "tests" in obj: return "Law"
    if "type" in obj and "tm_baseline" in obj: return "Location"
    if "class" in obj and "lesson" in obj: return "Monster"
    if "lineage" in obj or "patrons" in obj: return "Character"
    if "year" in obj and "title" in obj: return "Event"
    if "competence" in obj and "deity" in obj: return "Epiclesis"
    if "keywords" in obj and "invariants" in obj: return "Domain"
    return None

def main():
    ap = argparse.ArgumentParser(description="Lore Linter — valida item contro lo schema e regole base.")
    ap.add_argument("paths", nargs="+", help="File YAML/JSON da validare")
    args = ap.parse_args()

    schema = json.loads(open(SCHEMA_PATH, "r", encoding="utf-8").read())
    ok = True
    for path in args.paths:
        obj = load(path)
        t = guess_type(obj)
        if not t:
            print(f"[WARN] {path}: impossibile inferire tipo (skippato).")
            continue
        sub = {"$ref": f"#/$defs/{t}"}
        try:
            Draft202012Validator(schema).validate(obj, sub)
            print(f"[OK] {path}: {t} conforme allo schema.")
        except jsex.ValidationError as e:
            ok = False
            print(f"[ERR] {path}: {t} schema violation → {e.message}")
        # Extra checks
        status = obj.get("status")
        if status not in {"draft","proposal","canon","deprecated"}:
            ok = False
            print(f"[ERR] {path}: status mancante o non valido.")
        if t == "Ritual":
            if obj.get("expected_IE", 0) < 0:
                ok = False
                print(f"[ERR] {path}: expected_IE negativo.")
        if t == "Artifact":
            if "price" not in obj:
                ok = False
                print(f"[ERR] {path}: artifact senza 'price' (prezzo/costo d'uso).")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
