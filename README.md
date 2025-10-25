
# epiclesis-engine

Scientifically-grounded **Greek mythos** knowledge base + **RAG** toolkit.
Operational model: **Anánkē** (physical constraints), **epiclesis** and **domains**, **IE** (Epiphany Index), **tīmē/miasma** and **Lex Stygia**.

## What's inside
- 📚 Structured KB (YAML/MD) for narrative and RPGs
- 🧰 Tools: multi-provider runner, RAG, YAML validators, golden prompts
- 🔁 CI: GitHub Actions to test goldens and attach CSV reports

## Quick start
1. Download `kb_project_consolidated.zip` or clone the repo.
2. Export the keys (see `kb/tools/config/*.example`).
3. Run a golden:

```bash
  make golden-openai K=12 TEMP=0.8
  make validate-yaml
  make eval-report
```

4. See output in `kb/out/golden/<provider>/` and reports in `kb/eval/golden_results.csv`.

## License

MIT (content and tooling). If you prepare a commercial edition, cite the project and maintain credits.

