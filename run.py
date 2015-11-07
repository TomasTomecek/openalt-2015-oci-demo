#!/usr/bin/python3

import subprocess
import sys

try:
    F = int(sys.argv[1])
except IndexError:
    F = 8000

try:
    T = int(sys.argv[2])
except IndexError:
    T = F + 16


for x in range(F, T):
    cmd = [
        "docker",
        "run",
        "-d",
        "--net=host",
        "httpd",
        "httpd",
        "-DFOREGROUND",
        "-c", "Listen %d" % x
    ]
    subprocess.check_call(cmd)

