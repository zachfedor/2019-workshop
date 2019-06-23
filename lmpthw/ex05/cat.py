# Exercise 05

# 2019-06-22
# Reproducing the `cat` Command in Python

import argparse

parser = argparse.ArgumentParser()

numbering = parser.add_mutually_exclusive_group()
numbering.add_argument("-n", help="numbers each line of the output", action="store_true")
numbering.add_argument("-b", help="numbers each non-blank line of the output", action="store_true")

parser.add_argument("-e", help="display '$' character at end of lines", action="store_true")
parser.add_argument("filenames", help="any number of filenames to print out", nargs="*")

args = parser.parse_args()

concatenated = ""
for filename in args.filenames:
    with open(filename, 'r') as f:
        counter = 1
        for line in f.readlines():
            if (args.b and line != "\n") or args.n:
                concatenated += f"   {counter}\t"
                counter += 1

            if args.e:
                line = line.replace('\n', '$\n')

            concatenated += line

print(concatenated)

