# Golden suite — Istruzioni d'uso

## 1) Preparazione
- Installa dipendenze (`pip install -r requirements.txt` se presente; altrimenti `openai anthropic google-generativeai cohere pyyaml` in base al provider).
- Esporta le chiavi del provider (vedi `kb/tools/config/*.example`).

## 2) Esegui i Golden
Esempi con **Makefile**:
```bash
# OpenAI-compat (OpenAI, Groq, xAI, vLLM...)
make golden-openai K=12 TEMP=0.8

# Anthropic
make golden-anthropic

# Gemini
make golden-gemini

# Cohere
make golden-cohere
```
Gli output finiscono in `kb/out/golden/<provider>/...out.md`

## 3) Estrai e valida YAML (golden 02,04,08)
```bash
make validate-yaml
```
- Estrae il **primo code block YAML** dagli output (`extract_yaml.py`)
- Valida i campi minimi con `validate_yaml.py`:
  - 02 → `ritual`
  - 04 → `contract`
  - 08 → `artifact`

## 4) Report CSV
```bash
make eval-report
```
Apre/aggiorna `kb/eval/golden_results.csv` con righe: **date, provider, model, golden_id, file, yaml_found, yaml_valid, status, notes**.

## 5) Suggerimenti pratici
- Se il modello non usa i fence ```yaml, correggi il prompt o usa il validatore con `any` e revisiona a mano.
- Aggiungi note di valutazione direttamente nel CSV.
- Integra `make golden-...` in CI per regression test dei provider.
