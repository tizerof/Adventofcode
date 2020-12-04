def count_trees_first(file_name):
    """
    Find the number of trees with a step
    of 3 to the right and 1 down.
    """
    road = open(file_name).read().split("\n")
    counter = 3
    count_trees = 0
    for line in road[1:]:
        if line[counter] == "#":
            count_trees +=1
        counter = (counter + 3) % len(line)
    return count_trees


def count_trees_second(file_name):
    """
    Find multiply together the number of trees
    encountered on each of the listed slopes.
    """
    road = open(file_name).read().split("\n")
    result = 1
    for r,d in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
        counter = r
        count_trees = 0
        for line in road[d::d]:
            if line[counter] == "#":
                count_trees +=1
            counter = (counter + r) % len(line)
        result *= count_trees
    return result

print(count_trees_first("input.txt"))
print(count_trees_second("input.txt"))