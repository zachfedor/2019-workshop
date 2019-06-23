# Exercise 06

# 2019-06-23
# Reproducing the `find` Command in Python

import argparse
import glob
import os
import subprocess

parser = argparse.ArgumentParser()

action = parser.add_mutually_exclusive_group()
action.add_argument("-print", help="print out matching filenames (default action)", action="store_true", default=True)
action.add_argument("-exec", help="run command on matching filenames")

filtering = parser.add_mutually_exclusive_group()
filtering.add_argument("-name", help="match files by name, wildcards allowed (default filter)", default="*")
filtering.add_argument("-type", help="match files by type", choices=['d', 'f'])

parser.add_argument("path", help="path to search for files")

args = parser.parse_args()

if args.type:
    if args.type == 'f':
        matches = filter(lambda x: x.is_file(), os.scandir(args.path))
    elif args.type == 'd':
        matches = filter(lambda x: x.is_dir(), os.scandir(args.path))

    matches = map(lambda x: x.name, matches)
else:
    matches = glob.glob(os.path.join(args.path, args.name))

for match in matches:
    if args.exec:
        command = args.exec.split(' ')
        command.append(match)
        subprocess.call(command)
    elif args.print:
        print(match)

