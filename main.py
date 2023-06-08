#!/usr/bin/env python3

import shutil
import psutil
import os
from netw import *


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    print("CPU usage through out this function: {0}\nProcess ID: {1}".format(
        psutil.cpu_times(), os.getpid()))
    usage = psutil.cpu_percent(1)
    return usage < 50


if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR: Not enough disk space.")
elif check_localhost() and check_connectivity():
    print("Everything is good.")
else:
    print("Network health check failed.")
