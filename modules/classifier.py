import re
from llm.client import client
from config import MODEL

def classify_incident(text):
    prompt = f"""
    Classify this incident into:
    CPU / Memory / Network / Service

    Incident: {text}
    """

    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    output = resp.choices[0].message.content.strip()

    # Remove <think>...</think> sections
    output = re.sub(r"<think>.*?</think>", "", output, flags=re.DOTALL).strip()

    return output
