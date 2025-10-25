# Makefile — Golden prompts, validazione YAML, report
# Usa: make golden-openai  (prima esporta le chiavi, vedi kb/tools/config/*.example)

KB?=kb
OUT?=$(KB)/out/golden
K?=12
TEMP?=0.8

# Cartelle
TOOLS=$(KB)/tools
GOLDEN=$(KB)/prompts/golden
EVAL=$(KB)/eval

# Provider
PROVIDER?=openai

.PHONY: golden-openai golden-anthropic golden-gemini golden-cohere validate-yaml eval-report

golden-openai:
	python $(TOOLS)/golden_runner.py --provider openai --kb $(KB) --k $(K) --out $(OUT) --temperature $(TEMP)

golden-anthropic:
	python $(TOOLS)/golden_runner.py --provider anthropic --kb $(KB) --k $(K) --out $(OUT) --temperature $(TEMP)

golden-gemini:
	python $(TOOLS)/golden_runner.py --provider gemini --kb $(KB) --k $(K) --out $(OUT) --temperature $(TEMP)

golden-cohere:
	python $(TOOLS)/golden_runner.py --provider cohere --kb $(KB) --k $(K) --out $(OUT) --temperature $(TEMP)

# Estrai e valida YAML per i golden che lo richiedono (02=ritual, 04=contract, 08=artifact)
validate-yaml:
	@echo "== Estrazione YAML dai golden =="
	@for F in $(OUT)/*/02_* *.md; do :; done  # noop, lascia gli echo
	@for D in $(OUT)/*; do \
	  for F in $$D/02_* *.md $$D/04_* *.md $$D/08_* *.md; do \
	    if [ -f "$$F" ]; then \
	      Y=$${F%.md}.yaml; \
	      python $(TOOLS)/extract_yaml.py "$$F" "$$Y" || true; \
	      if [ -f "$$Y" ]; then \
	        case "$$F" in \
	          *02_*) python $(TOOLS)/validate_yaml.py "$$Y" ritual || true ;; \
	          *04_*) python $(TOOLS)/validate_yaml.py "$$Y" contract || true ;; \
	          *08_*) python $(TOOLS)/validate_yaml.py "$$Y" artifact || true ;; \
	        esac; \
	      fi; \
	    fi; \
	  done; \
	done

# Report (append) — leggi i risultati e aggiorna CSV
eval-report:
	python $(TOOLS)/eval_report.py --out $(OUT) --csv $(EVAL)/golden_results.csv
