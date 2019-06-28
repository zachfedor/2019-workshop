# Exercise 07

# 2019-06-24
# Reproducing the `grep` Command in Python

import argparse
import glob
import re

parser = argparse.ArgumentParser()
parser.add_argument("pattern", help="pattern to search within files")
parser.add_argument("files", help="at least one file name or pattern", nargs="+")

args = parser.parse_args()

def find_files(files):
    return [item for sublist in [glob.glob(f) for f in files] for item in sublist]

def grep(pattern, files):
    p = re.compile(pattern)

    matches = []
    for f in find_files(files):
        with open(f) as contents:
            for line in contents.readlines():
                if p.search(line):
                    print(f"{f}:{line}", end="")

grep(args.pattern, args.files)

