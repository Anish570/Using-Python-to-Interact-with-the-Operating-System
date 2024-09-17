#!/usr/bin/env python3
import shutil
import psutil


du = shutil.disk_usage("/")
print("Free disk usage:",du.free/du.total*100)

cpu_percent = psutil.cpu_percent(0.1)
print("CPU usage:", cpu_percent)

