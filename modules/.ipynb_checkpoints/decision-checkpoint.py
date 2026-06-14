from tools.metrics import get_cpu, get_memory, get_disk
from tools.actions import restart_service
from config import CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD


def decide_action(category=None):
    cpu = get_cpu()
    memory = get_memory()
    disk = get_disk()
    # ✅ CPU logic
    if category == "CPU":
        if cpu > CPU_THRESHOLD:
            return f"""Suggested Action: System Restart

CPU ({cpu}%) - Critical"""
        else:
            return f"""Suggested Action: No action required

CPU ({cpu}%) - Normal
Memory ({memory}%) - Normal
Disk ({disk}%)- Normal"""

    # ✅ Memory logic
    if category == "Memory":
        if memory > MEMORY_THRESHOLD:
            return f"""Suggested Action: Restart Service

Memory ({memory}%) - Critical"""
        else:
            return f"""Suggested Action: No action required

CPU ({cpu}%) - Normal
Memory ({memory}%) - Normal
sk ({disk}%) - Normal"""

    # ✅ Disk logic
    if category == "Disk":
        if disk > DISK_THRESHOLD:
            return f"""Suggested Action: Clean Disk

Disk ({disk}%) - Critical"""
        else:
            return f"""Suggested Action: No action required

CPU ({cpu}%) - Normal
Memory ({memory} - Normal
Disk ({disk}%) - Normal"""

    # ✅ Fallback (multi-metric check)
    if cpu > CPU_THRESHOLD:
        return f"""Suggested Action: System Restart

CPU ({cpu}%) - Critical"""

    if memory > MEMORY_THRESHOLD:
        return f"""Suggested Action: Restart Service

Memory ({memory}%) - Critical"""

    if disk > DISK_THRESHOLD:
        return f"""Suggeed Action: Clean Disk

Disk ({disk}%) - Critical"""

    # ✅ Fully healthy system
    return f"""Suggested Action: No action required

CPU ({cpu}%) - Normal
Memory ({memory}%) - Normal
Disk ({disk}%) - Normal"""