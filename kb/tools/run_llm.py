#!/usr/bin/env python3
"""
run_llm.py — Costruisce un prompt via RAG e chiama un LLM.
Prerequisiti:
  pip install openai requests pyyaml
Env attesi:
  OPENAI_API_KEY          # chiave
  OPENAI_MODEL            # es. "gpt-4o-mini" (o altro modello compatibile)
  OPENAI_BASE (opzionale) # endpoint alternativo compatibile OpenAI
Uso:
  python kb/tools/run_llm.py --kb kb --query "tregua in porto conteso (Ermes+Poseidone)" --k 10
  python kb/tools/run_llm.py --prompt-file prompt.txt
"""
import os, argparse, sys
from pathlib import Path

# Importiamo il builder dal rag_demo
sys.path.append(str(Path(__file__).resolve().parent))
from rag_demo import build_prompt

def call_openai(prompt: str) -> str:
    # prova con SDK ufficiale, altrimenti fallback su requests
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_BASE"))
        model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
        # chat.completions stile moderno
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role":"system","content":"Sei un autore/GM per l'universo mitologico-scientifico greco. Rispetta Anánkē, T/M/IE, Lex Stygia."},
                {"role":"user","content": prompt}
            ],
            temperature=0.8,
        )
        return resp.choices[0].message.content
    except Exception as e:
        # Fallback HTTP grezzo
        import requests, json
        api_key = os.environ.get("OPENAI_API_KEY")
        base = os.environ.get("OPENAI_BASE","https://api.openai.com/v1")
        model = os.environ.get("OPENAI_MODEL","gpt-4o-mini")
        if not api_key:
            return f"[ERRORE] OPENAI_API_KEY mancante. Prompt pronto ma non inviato.\n\n{prompt}"
        url = f"{base}/chat/completions"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type":"application/json"}
        payload = {
            "model": model,
            "messages":[
                {"role":"system","content":"Sei un autore/GM per l'universo mitologico-scientifico greco. Rispetta Anánkē, T/M/IE, Lex Stygia."},
                {"role":"user","content": prompt}
            ],
            "temperature":0.8
        }
        r = requests.post(url, headers=headers, json=payload, timeout=60)
        if r.status_code != 200:
            return f"[ERRORE API] {r.status_code} {r.text}\n\nPrompt:\n{prompt}"
        data = r.json()
        return data["choices"][0]["message"]["content"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", default="kb")
    ap.add_argument("--query", help="richiesta da trasformare in prompt RAG")
    ap.add_argument("--k", type=int, default=10)
    ap.add_argument("--status", nargs="+", default=["canon","proposal"])
    ap.add_argument("--prompt-file", help="usa un prompt già pronto")
    ap.add_argument("--print-only", action="store_true", help="non chiamare l'LLM, stampa solo il prompt")
    args = ap.parse_args()

    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding="utf-8")
    elif args.query:
        prompt = build_prompt(args.kb, args.query, args.k, tuple(args.status))
    else:
        print("Usa --query o --prompt-file", file=sys.stderr); sys.exit(1)

    if args.print_only:
        print(prompt); return

    output = call_openai(prompt)
    print(output)

if __name__ == "__main__":
    main()
