# Minimal Anthropic adapter
import os, json

def call(model: str, prompt: str, temperature: float = 0.8):
    """
    Returns text using Anthropic Messages.
    Env: ANTHROPIC_API_KEY, ANTHROPIC_MODEL (optional)
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    model = model or os.environ.get("ANTHROPIC_MODEL", "claude-3-5-sonnet-latest")
    if not api_key:
        return "[ERR] ANTHROPIC_API_KEY missing.\n\n" + prompt

    try:
        from anthropic import Anthropic
        client = Anthropic(api_key=api_key)
        msg = client.messages.create(
            model=model,
            max_tokens=2048,
            temperature=temperature,
            messages=[
                {"role":"user","content": prompt}
            ]
        )
        return "".join([c.text for c in msg.content if hasattr(c, "text")])
    except Exception as e:
        # Fallback REST
        import requests
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        payload = {
            "model": model,
            "max_tokens": 2048,
            "temperature": temperature,
            "messages":[{"role":"user","content": prompt}]
        }
        r = requests.post(url, headers=headers, json=payload, timeout=60)
        if r.status_code != 200:
            return f"[ERR Anthropic] {r.status_code} {r.text}\n\nPrompt:\n{prompt}"
        data = r.json()
        # newer API returns in content list
        parts = data.get("content", [])
        texts = []
        for p in parts:
            if p.get("type") == "text":
                texts.append(p.get("text",""))
        return "".join(texts) or json.dumps(data)
