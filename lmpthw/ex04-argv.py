# Exercise 04

# 2019-05-17
# Dealing w/ Command Line Arguments using `sys.argv`

import sys

greeting = 'Hello'
end = "\n"
name = ""
dups = 1
pos_args = []

for option in sys.argv[1:]:
    if '-s' == option:
        greeting = 'Hi'
    elif '-l' == option:
        greeting = 'Hail and well met'
    elif '-one-line' == option:
        end = ""
    elif '-n=' == option[:3]:
        name = f", {option[3:]}"
    elif '-d=' == option[:3]:
        dups = int(option[3:])
    elif '-' != option[0]:
        pos_args.append(option)
        
for i in range(dups):
    if end == "" and i < dups - 1:
        print(f"{greeting}{name}! ", end=end)
    else:
        print(f"{greeting}{name}!", end=end)

if pos_args:
    print(f"You have attempted to print the following files: {pos_args}")
