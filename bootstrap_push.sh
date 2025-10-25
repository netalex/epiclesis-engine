#!/usr/bin/env bash
set -euo pipefail

# === Config ===
REMOTE="${REMOTE:-git@github.com:netalex/epiclesis-engine.git}"
BRANCH="${BRANCH:-main}"
ZIP_CONSOLIDATED="${ZIP_CONSOLIDATED:-kb_project_consolidated.zip}"

echo "Repo remote: $REMOTE"
echo "Target branch: $BRANCH"

# 1) Init repo if needed
if [ ! -d .git ]; then
  echo "[*] git init"
  git init
fi

# 2) Remote
if git remote get-url origin >/dev/null 2>&1; then
  echo "[*] origin already set → $(git remote get-url origin)"
  git remote set-url origin "$REMOTE"
else
  echo "[*] set origin → $REMOTE"
  git remote add origin "$REMOTE"
fi

# 3) Ensure user identity (optional)
if ! git config user.name >/dev/null; then
  echo "[i] Set your identity with: git config user.name 'Your Name'"
fi
if ! git config user.email >/dev/null; then
  echo "[i] Set your email with: git config user.email 'you@example.com'"
fi

# 4) Fetch remote branch if exists
echo "[*] fetching origin/$BRANCH (if exists)"
git fetch origin "$BRANCH" || true

# 5) Checkout branch and rebase onto remote if present
echo "[*] checkout -B $BRANCH"
git checkout -B "$BRANCH"
if git rev-parse --verify origin/"$BRANCH" >/dev/null 2>&1; then
  echo "[*] rebase on origin/$BRANCH (if any commits)"
  git pull --rebase origin "$BRANCH" || true
fi

# 6) Optional: add helper files if missing
if [ ! -f ".gitignore" ]; then
cat > .gitignore <<'EOF'
# Python
__pycache__/
*.pyc
.venv/
.env
# Editors/OS
.vscode/
.idea/
.DS_Store
# Output (generated)
kb/out/
kb/eval/golden_results.csv
# Archives
*.zip
EOF
  echo "[*] wrote .gitignore"
fi

if [ ! -f "LICENSE" ]; then
cat > LICENSE <<'EOF'
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF
  echo "[*] wrote LICENSE (MIT)"
fi

# 7) Stage, commit, push
echo "[*] staging files"
git add -A

if git diff --cached --quiet; then
  echo "[i] nothing to commit."
else
  git commit -m "Add mythos lore KB + RAG toolkit + Golden CI"
fi

echo "[*] pushing to origin/$BRANCH"
git push -u origin "$BRANCH"

echo "[✓] Done."
echo "If you want to publish the consolidated ZIP as a GitHub Release:"
echo "  gh release create v0.1.0 \"
echo "    $ZIP_CONSOLIDATED -t 'v0.1.0' -n 'Initial seed: KB + tools + CI'"
