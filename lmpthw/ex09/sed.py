# Exercise 09

# 2019-07-05
# Reproducing the `sed` command in Python

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="path to file")
parser.add_argument("-e", help="substitution command to run on stream")
args = parser.parse_args()


command, target, substitute, flags = args.e.split('/')

with open(args.file) as f:
    for line in f.readlines():
        count = 0 if flags == 'g' else 1
        line = re.sub(target, substitute, line, count)
        print(line, end="")

