#!/usr/bin/env python3
import sys
import subprocess

f = open(sys.argv[1], 'r')

for line in f.readlines():
    old_name = line.strip()
    name = old_name.replace("jane", "jdoe")
    subprocess.run(["mv", old_name, name])
f.close()
