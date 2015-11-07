#!/usr/bin/python3

import sys
import requests
from multiprocessing import Pool

def bombard():
    while True:
        try:
            requests.get("http://localhost/")
        except KeyboardInterrupt:
            pass

try:
    N_THREADS = sys.argv[1]
except IndexError:
    N_THREADS = 4

e = Pool(processes=N_THREADS)
try:
    f = e.apply(bombard)
except KeyboardInterrupt:
    pass
