#!/usr/bin/env python3
"""
rag_demo.py — Retrieval & Prompt Builder minimale per la KB della lore.
Uso:
  python kb/tools/rag_demo.py --kb kb --query "pace tra quartieri, rito cittadino" --k 8 --status canon proposal --out prompt.txt
"""
import argparse, os, json, yaml, glob, textwrap, sys, pathlib

def load_items(kb_root):
    paths = []
    for ext in ("*.yaml","*.yml","*.json"):
        paths += glob.glob(os.path.join(kb_root, "**", ext), recursive=True)
    items = []
    for p in paths:
        try:
            with open(p, "r", encoding="utf-8") as f:
                if p.endswith(".json"):
                    obj = json.load(f)
                else:
                    obj = yaml.safe_load(f)
        except Exception as e:
            # skip broken files
            continue
        obj["_path"] = p
        obj["_type"] = p.split(os.sep)[-2]  # es. 'deities','rituals'
        items.append(obj)
    return items

def tokenize(s):
    return [w.lower() for w in (s or "").replace("/", " ").replace("-", " ").split()]

def item_text(obj):
    # Sviluppiamo un testo di indicizzazione
    fields = []
    for k in ("id","name","title","summary","description"):
        if k in obj and isinstance(obj[k], str):
            fields.append(obj[k])
    for k in ("keywords","domains","competence","anchors","policies","offers"):
        if k in obj and isinstance(obj[k], list):
            fields.extend([str(x) for x in obj[k]])
    return " ".join(fields)

def score_item(obj, q_tokens):
    text = item_text(obj).lower()
    score = 0
    for t in q_tokens:
        if t in text:
            score += 1
    # boost by type
    if obj["_type"] in {"rituals","epicleses","laws"}:
        score += 0.5
    return score

def build_context_snippet(obj, maxlen=420):
    tid = obj.get("id","(no-id)")
    ttype = obj.get("_type","?")
    name = obj.get("name") or obj.get("title") or tid
    status = obj.get("status","")
    # compact summary
    if "summary" in obj and obj["summary"]:
        summary = obj["summary"]
    elif "description" in obj and obj["description"]:
        summary = obj["description"]
    else:
        summary = ""
    # key fields
    keys = []
    for k in ("domains","competence","policies","offers","anchors","tm_effect","rule"):
        v = obj.get(k)
        if v:
            if isinstance(v, list):
                v = ", ".join([str(x) for x in v[:6]])
            elif isinstance(v, dict):
                v = ", ".join([f"{kk}:{vv}" for kk,vv in list(v.items())[:6]])
            keys.append(f"{k}={v}")
    blob = f"[{ttype}] {name}  <{tid}>  (status:{status})\n{summary}\n" + ("; ".join(keys))
    return blob[:maxlen]

def build_prompt(kb_root, query, k=8, statuses=("canon","proposal")):
    items = load_items(kb_root)
    q_tokens = tokenize(query)
    filt = [it for it in items if it.get("status") in statuses]
    scored = sorted(((score_item(it,q_tokens), it) for it in filt), key=lambda x: x[0], reverse=True)
    tops = [it for s,it in scored if s>0][:k]
    # System
    sys_path = os.path.join(kb_root, "prompts", "system.lore.txt")
    system_text = open(sys_path,"r",encoding="utf-8").read() if os.path.exists(sys_path) else ""
    # Context
    ctx = "\n\n".join(build_context_snippet(it) for it in tops)
    # Task wrapper
    prompt = f"""### SYSTEM
{system_text.strip()}

### CONTEXT (RAG)
{ctx}

### TASK
Scrivi contenuto coerente con la lore in base alla richiesta seguente. Indica IE e costi quando applicabile, evita violazioni di Anánkē.

Richiesta: {query}
"""
    return prompt

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", default="kb", help="radice KB")
    ap.add_argument("--query", required=True, help="richiesta dell'utente")
    ap.add_argument("--k", type=int, default=8, help="quanti item recuperare")
    ap.add_argument("--status", nargs="+", default=["canon","proposal"], help="stati ammessi")
    ap.add_argument("--out", default=None, help="salva prompt su file")
    args = ap.parse_args()

    prompt = build_prompt(args.kb, args.query, args.k, tuple(args.status))
    if args.out:
        with open(args.out,"w",encoding="utf-8") as f:
            f.write(prompt)
        print(f"[OK] Prompt salvato in {args.out}")
    else:
        print(prompt)

if __name__ == "__main__":
    main()
