# Minimal Gemini REST adapter
import os, json

def call(model: str, prompt: str, temperature: float = 0.8):
    """
    Returns text using Google Gemini REST (generateContent).
    Env: GEMINI_API_KEY, GEMINI_MODEL (optional)
    """
    key = os.environ.get("GEMINI_API_KEY")
    model = model or os.environ.get("GEMINI_MODEL", "gemini-2.0-pro-exp-02")
    if not key:
        return "[ERR] GEMINI_API_KEY missing.\n\n" + prompt

    import requests
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    payload = {
      "contents":[
        {"role":"user","parts":[{"text": prompt}]}
      ],
      "generationConfig":{
        "temperature": temperature
      }
    }
    r = requests.post(url, json=payload, timeout=60)
    if r.status_code != 200:
        return f"[ERR Gemini] {r.status_code} {r.text}\n\nPrompt:\n{prompt}"
    data = r.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return json.dumps(data)
