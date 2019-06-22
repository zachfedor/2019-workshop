# Exercise 05

# 2019-06-22
# Reproducing the `cat` Command in Python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filenames", help="any number of filenames to print out", nargs="*")


args = parser.parse_args()
concatenated = ""
for filename in args.filenames:
    with open(filename, 'r') as f:
        concatenated += f.read()

print(concatenated)

