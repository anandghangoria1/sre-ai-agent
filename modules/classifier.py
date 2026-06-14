import re
from llm.client import client
from config import MODEL

def classify_incident(text):
    prompt = f"""
    Classify this incident into:
    CPU / Memory / Network / Service

    Only return one word.

    Incident: {text}
    """

    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    output = resp.choices[0].message.content

    # Remove <think>...</think>
    output = re.sub(r"<think>.*?</think>", "", output, flags=re.DOTALL)

    output = output.strip()

    # Extract first word
    category = output.split()[0]

    return category
