#!/usr/bin/env python3
"""
golden_runner.py — esegue i Golden Prompts con un provider e salva gli output.
Requisiti: le variabili d'ambiente del provider (vedi kb/tools/config/*.example)
Uso:
  python kb/tools/golden_runner.py --provider openai --kb kb --k 12 --out kb/out/golden/openai
  python kb/tools/golden_runner.py --provider anthropic --subset 02,04,08
"""
import os, argparse, subprocess, sys, datetime
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", required=True, choices=["openai","anthropic","gemini","cohere"])
    ap.add_argument("--kb", default="kb")
    ap.add_argument("--k", type=int, default=12)
    ap.add_argument("--out", default="kb/out/golden")
    ap.add_argument("--subset", help="es: 02,04,08 per eseguire solo alcuni golden")
    ap.add_argument("--model", default="")
    ap.add_argument("--temperature", type=float, default=0.8)
    args = ap.parse_args()

    base = Path(__file__).resolve().parent.parent
    prompts_dir = base / "prompts" / "golden"
    outdir = Path(args.out) / args.provider
    outdir.mkdir(parents=True, exist_ok=True)

    selected = None
    if args.subset:
        selected = set([s.strip() for s in args.subset.split(",") if s.strip()])

    files = sorted(prompts_dir.glob("*.md"))
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    for fp in files:
        stem = fp.stem
        if selected and not any(stem.startswith(x) for x in selected):
            continue
        out_file = outdir / f"{stem}.{ts}.out.md"

        cmd = [
            sys.executable, str(base/"tools"/"run_llm_any.py"),
            "--provider", args.provider,
            "--kb", str(base),
            "--prompt-file", str(fp),
            "--k", str(args.k)
        ]
        if args.model: cmd += ["--model", args.model]
        if args.temperature is not None: cmd += ["--temperature", str(args.temperature)]
        print("RUN:", " ".join(cmd))
        result = subprocess.run(cmd, capture_output=True, text=True)
        out_file.write_text(result.stdout if result.stdout else result.stderr, encoding="utf-8")
        print("WROTE:", out_file)

    print("Done. Output in:", outdir)

if __name__ == "__main__":
    main()
