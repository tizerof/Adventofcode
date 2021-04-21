class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(vertex):
    while vertex:
        print(vertex.value)
        vertex = vertex.next_item


n3 = Node('third')
n2 = Node('second', n3)
n1 = Node('first', n2)
solution(n1)
