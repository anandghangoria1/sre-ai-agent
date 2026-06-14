import re
from llm.client import client
from config import MODEL
from tools.metrics import get_cpu, get_memory, get_disk

def analyze_incident(text):
    cpu = get_cpu()
    memory = get_memory()
    disk = get_disk()

    prompt = f"""
    You are an SRE expert.

    Incident: {text}

    Current System Metrics:
    CPU: {cpu}%
    Memory: {memory}%
    Disk: {disk}%

    Analyze whether the incident is valid based on the system metrics.

    Provide:
    1. Root cause
    2. Suggested fix

    If the system is normal, clearly say no issue detected.

    Do not include thinking steps.
    """

    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    output = resp.choices[0].message.content

    # Correct removal of <think> blocks
    output = re.sub(r"<think>.*?</think>", "", output, flags=re.DOTALL)

    return output.strip()