# Exercise 08

# 2019-06-28
# Reproducing the `cut` Command in Python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="path to file")

action = parser.add_mutually_exclusive_group()
action.add_argument("-c", help="index of character(s)")
action.add_argument("-f", help="field of delimited list")
parser.add_argument("-d", help="delimiter to split string into fields")

args = parser.parse_args()


def parse_index(string):
    # NOTE: must subtract 1 from ordinal input to switch to 0-indexing of strings
    index = None

    try:
        if ',' in string:
            elements = string.split(',')
            index = list(map(lambda x: int(x) - 1, elements))
            index.sort()
        elif '-' in string:
            start_end = string.split('-')
            index = list(range(int(start_end[0]) - 1, int(start_end[1])))
        else:
            index = int(string) - 1
    except ValueError:
        print('Error: illegal list value for -c option')
        exit(1)

    return index


with open(args.file) as f:
    if args.c:
        index = parse_index(args.c)
    elif args.f:
        index = parse_index(args.f)

    for line in f.readlines():
        if args.f:
            line = line.split(args.d)

        if type(index) is list:
            output = ''
            for i in index:
                if i <= len(line):
                    if output != '':
                        output += args.d
                    output += line[i]
            print(output, end="")
        elif type(index) is int:
            if index <= len(line):
                print(line[index])

