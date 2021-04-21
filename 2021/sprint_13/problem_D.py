class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def print_list(vertex):
    while vertex:
        print(vertex.value)
        vertex = vertex.next_item


def solution(node, elem):
    count = 0
    while node:
        if node.value == elem:
            return count
        node = node.next_item
        count += 1
    return -1


n6 = Node('6')
n5 = Node('5', n6)
n4 = Node('4', n5)
n3 = Node('3', n4)
n2 = Node('2', n3)
n1 = Node('1', n2)
print(solution(n1, n5))
