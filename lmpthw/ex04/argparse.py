# Exercise 04

# 2019-05-17
# Dealing w/ Command Line Arguments using `argparse` library

import argparse

parser = argparse.ArgumentParser()

length = parser.add_mutually_exclusive_group()
length.add_argument("-s", "--short", help="print a shorter greeting", action="store_true")
length.add_argument("-l", "--long", help="print a longer greeting", action="store_true")

parser.add_argument("-o", "--oneline", help="don't print a new line at end of string", action="store_true")
parser.add_argument("-d", "--dups", help="duplicate the greeting a given number of times", type=int, default=1)

parser.add_argument("-n", "--name", help="print a name with the greeting")

parser.add_argument("files", help="any number of filenames to print out", nargs="*")

args = parser.parse_args()

if args.short:
    greeting = "Hi"
elif args.long:
    greeting = "Hail and well met"
else:
    greeting = "Hello"

name = f", {args.name}" if args.name else ""
end = "" if args.oneline else "\n"

for i in range(args.dups):
    print(f"{greeting}{name}!", end=end)

if args.files:
    print("You have attempted to print the following files:")
    for f in args.files:
        print(f"- {f}")
