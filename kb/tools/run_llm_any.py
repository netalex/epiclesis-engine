#!/usr/bin/env python3
"""
run_llm_any.py — Runner unificato per provider:
- openai-compat (OpenAI, Groq, xAI, vLLM, Together...)
- anthropic (Claude)
- gemini (Google)
- cohere (Command)

Uso:
  # OpenAI-compat
  export OPENAI_API_KEY=...; export OPENAI_MODEL=...; export OPENAI_BASE=https://api.groq.com/openai/v1
  python kb/tools/run_llm_any.py --provider openai --kb kb --query "..."

  # Anthropic
  export ANTHROPIC_API_KEY=...; export ANTHROPIC_MODEL=claude-3-5-sonnet-latest
  python kb/tools/run_llm_any.py --provider anthropic --kb kb --query "..."

Args comuni: --kb, --query, --k, --status, --model, --temperature, --prompt-file, --print-only
"""
import os, argparse, sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from rag_demo import build_prompt

def call_openai(prompt: str, model: str = "", temperature: float = 0.8) -> str:
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_BASE"))
        model = model or os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role":"system","content":"Sei un autore/GM per l'universo mitologico-scientifico greco. Rispetta Anánkē, T/M/IE, Lex Stygia."},
                {"role":"user","content": prompt}
            ],
            temperature=temperature,
        )
        return resp.choices[0].message.content
    except Exception as e:
        import requests, json
        api_key = os.environ.get("OPENAI_API_KEY")
        base = os.environ.get("OPENAI_BASE","https://api.openai.com/v1")
        model = model or os.environ.get("OPENAI_MODEL","gpt-4o-mini")
        if not api_key:
            return f"[ERR] OPENAI_API_KEY missing.\n\n{prompt}"
        url = f"{base}/chat/completions"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type":"application/json"}
        payload = {
            "model": model,
            "messages":[
                {"role":"system","content":"Sei un autore/GM per l'universo mitologico-scientifico greco. Rispetta Anánkē, T/M/IE, Lex Stygia."},
                {"role":"user","content": prompt}
            ],
            "temperature":temperature
        }
        r = requests.post(url, headers=headers, json=payload, timeout=60)
        if r.status_code != 200:
            return f"[ERR OpenAI-compat] {r.status_code} {r.text}\n\nPrompt:\n{prompt}"
        data = r.json()
        return data["choices"][0]["message"]["content"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", required=True, choices=["openai","anthropic","gemini","cohere"])
    ap.add_argument("--kb", default="kb")
    ap.add_argument("--query")
    ap.add_argument("--k", type=int, default=10)
    ap.add_argument("--status", nargs="+", default=["canon","proposal"])
    ap.add_argument("--prompt-file")
    ap.add_argument("--model", default="")
    ap.add_argument("--temperature", type=float, default=0.8)
    ap.add_argument("--print-only", action="store_true")
    args = ap.parse_args()

    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding="utf-8")
    elif args.query:
        prompt = build_prompt(args.kb, args.query, args.k, tuple(args.status))
    else:
        print("Usa --query o --prompt-file", file=sys.stderr); sys.exit(1)

    if args.print_only:
        print(prompt); return

    provider = args.provider
    model = args.model
    temp = args.temperature

    if provider == "openai":
        out = call_openai(prompt, model, temp)
    elif provider == "anthropic":
        from adapters.anthropic_adapter import call as anth_call
        out = anth_call(model, prompt, temp)
    elif provider == "gemini":
        from adapters.gemini_adapter import call as gem_call
        out = gem_call(model, prompt, temp)
    elif provider == "cohere":
        from adapters.cohere_adapter import call as coh_call
        out = coh_call(model, prompt, temp)
    else:
        out = "[ERR] Provider non supportato."

    print(out)

if __name__ == "__main__":
    main()
