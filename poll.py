#! /usr/bin/env python3

import json
import socket

import psutil

B_TO_MB = 1024 * 1024


hostname = socket.gethostname()

cpu_usage = psutil.cpu_percent(interval=None)

mem  = psutil.virtual_memory()
free_ram_MB = round(mem[1] / B_TO_MB)
used_ram_MB = round(mem[3] / B_TO_MB)

output = {
    "node_name": hostname,
    "cpu_usage": cpu_usage,
    "free_ram_MB": free_ram_MB,
    "used_ram_MB": used_ram_MB
}

print(json.dumps(output))