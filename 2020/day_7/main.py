# https://adventofcode.com/2020/day/7


import re
from collections import defaultdict

def contained_in(color):
    """ Count how many bag colors can eventually
    contain at least one input color bag.
    """
    bags = defaultdict(set)
    for line in open("input.txt").readlines():
        parent, children = line.split(" bags contain ")
        for child in re.findall(r"(\w+ \w+) bags?", children):
            bags[child].add(parent)

    def outside(name):
        s = bags[name].copy()
        for bag in bags[name]:
            s.update(outside(bag))
        return s
    return len(outside(color))


def contained_out(color):
    """ Count how many individual bags are required
    inside one single input color bag.
    """
    bags = defaultdict(dict)
    for line in open("input.txt").readlines():
        parent, children = line.split(" bags contain ")
        for count, child in re.findall(r"(\d+) (\w+ \w+) bags?[,.]", children):
            bags[parent][child] = int(count)

    def inside(name):
        c = 0
        for bag, count in bags[name].items():
            c += count
            c += count * inside(bag)
        return c
    return inside(color)


print(contained_in("shiny gold"))
print(contained_out("shiny gold"))