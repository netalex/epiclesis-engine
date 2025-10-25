# Minimal Cohere Chat adapter
import os, json

def call(model: str, prompt: str, temperature: float = 0.8):
    """
    Returns text using Cohere Chat.
    Env: COHERE_API_KEY, COHERE_MODEL (optional)
    """
    key = os.environ.get("COHERE_API_KEY")
    model = model or os.environ.get("COHERE_MODEL", "command-r-plus")
    if not key:
        return "[ERR] COHERE_API_KEY missing.\n\n" + prompt

    try:
        import cohere
        co = cohere.Client(api_key=key)
        resp = co.chat(model=model, message=prompt, temperature=temperature)
        return resp.text or ""
    except Exception as e:
        # Fallback REST
        import requests
        url = "https://api.cohere.com/v1/chat"
        headers = {"Authorization": f"Bearer {key}", "Content-Type":"application/json"}
        payload = {"model": model, "message": prompt, "temperature": temperature}
        r = requests.post(url, headers=headers, json=payload, timeout=60)
        if r.status_code != 200:
            return f"[ERR Cohere] {r.status_code} {r.text}\n\nPrompt:\n{prompt}"
        data = r.json()
        return data.get("text","") or json.dumps(data)
