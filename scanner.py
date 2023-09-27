#! /usr/bin/env python3

import json

from scans import PingScan, ScanEncoder

targets = ["1.1.1.1", "8.8.8.8"]
scans = []

for target in targets:
    scan = PingScan(target)
    scan.scan()
    scans.append(scan)

with open("results.json", 'w') as json_file:
    scan_json = json.dump(scans, json_file, cls=ScanEncoder, indent=4)
    