import psutil

# CPU
def get_cpu():
    return round(psutil.cpu_percent(interval=1), 2)

# Memory
def get_memory():
    mem = psutil.virtual_memory()
    return round(mem.percent, 2)

# Disk
def get_disk():
    disk = psutil.disk_usage('/')
    return round(disk.percent, 2)