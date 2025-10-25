# Provider & Integrazione rapida

Questi file ti permettono di usare **lo stesso runner** (`run_llm_any.py`) con provider diversi.

## 1) OpenAI‑compat (OpenAI, Groq, xAI, vLLM, Together...)
- Carica `.env.openai.example` e personalizza `OPENAI_BASE` se serve.
- Esempi:
```bash
# Groq (Llama 70B)
export OPENAI_API_KEY=groq-...
export OPENAI_MODEL=llama-3.3-70b-versatile
export OPENAI_BASE=https://api.groq.com/openai/v1
python kb/tools/run_llm_any.py --provider openai --kb kb --query "tregua in porto conteso" --k 10

# vLLM self-host
export OPENAI_API_KEY=not-needed
export OPENAI_MODEL=meta-llama/llama-3.1-70b-instruct
export OPENAI_BASE=http://localhost:8000/v1
python kb/tools/run_llm_any.py --provider openai --kb kb --query "seedbook per Eleusi" --k 10
```

## 2) Anthropic (Claude)
```bash
export ANTHROPIC_API_KEY=sk-ant-...
export ANTHROPIC_MODEL=claude-3-5-sonnet-latest
python kb/tools/run_llm_any.py --provider anthropic --kb kb --query "rituale: sigillo sobrio" --k 8
```

## 3) Gemini (Google)
```bash
export GEMINI_API_KEY=AIza...
export GEMINI_MODEL=gemini-2.5-flash
python kb/tools/run_llm_any.py --provider gemini --kb kb --query "campagna breve porto conteso" --k 12
```

## 4) Cohere (Command)
```bash
export COHERE_API_KEY=cohere-...
export COHERE_MODEL=command-r-plus
python kb/tools/run_llm_any.py --provider cohere --kb kb --query "golden test: oracolo carestia" --k 6
```

### Opzioni comuni
- `--model` per forzare un modello diverso da quello in `.env`.
- `--temperature` (default 0.8).
- `--prompt-file` per usare un prompt già salvato.
- `--print-only` per stampare solo il prompt.

> Suggerimento: usa `direnv` o `dotenv` per gestire comode `.env` per provider.
