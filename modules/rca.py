from llm.client import client
from config import MODEL

def analyze_incident(text):
    prompt = f"""
    You are an SRE expert.

    Incident: {text}

    Provide:
    1. Root cause
    2. Suggested fix
    """

    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return resp.choices[0].message.content.strip()