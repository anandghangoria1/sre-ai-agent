from tools.metrics import get_cpu
from tools.actions import restart_service
from config import CPU_THRESHOLD

def decide_action():
    cpu = get_cpu()

    if cpu > CPU_THRESHOLD:
        return restart_service("nginx")
    return f"CPU normal ({cpu}%). No action"