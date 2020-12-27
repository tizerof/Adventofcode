# https://adventofcode.com/2020/day/8


import re

def find_acc(instructions):
    """ Find value in the accumulator with error or not.
    Returns:
        (bool, int)

        first is whether the instrument is correct, 
        the second is the last value of accumulator.
    """
    counter = ()
    err = False
    i = acc = 0
    while True:
        if i in counter:
            break
        if i > len(instructions)-1:
            err = True
        counter += (i,)
        try:
            operation, argument = instructions[i]
        except IndexError:
            break
        if operation == "acc":
            acc += int(argument)
        if operation == "jmp":
            i += int(argument)
            continue
        i += 1
    return (err, acc)


def find_acc_fixed(instructions):
    """ Swaps commands "jmp" and "nop", verifies instructions 
    with a function find_acc()
    """
    acc = 0
    for i, instruction in enumerate(instructions):
        operation, argument = instruction
        fixed = instructions.copy()
        if operation == "jmp":
            fixed[i] = ("nop", argument)
            err, acc = find_acc(fixed)
            if err:
                break
        if operation == "nop":
            fixed[i] = ("jmp", argument)
            err, acc = find_acc(fixed)
            if err:
                break
    return acc


instructions = re.findall(r"(\w+) ([+-]\d+)", open("input.txt").read())
print(find_acc(instructions))
print(find_acc_fixed(instructions))