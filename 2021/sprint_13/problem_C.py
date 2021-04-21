class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def print_list(vertex):
    while vertex:
        print(vertex.value)
        vertex = vertex.next_item


def solution(vertex, idx):
    count = 0
    if idx == 0:
        return vertex.next_item
    node = vertex
    while node:
        if count + 1 == idx:
            node.next_item = node.next_item.next_item
            break
        node = node.next_item
        count += 1
    return vertex


n6 = Node('6')
n5 = Node('5', n6)
n4 = Node('4', n5)
n3 = Node('3', n4)
n2 = Node('2', n3)
n1 = Node('1', n2)
print_list(solution(n1, 2))
