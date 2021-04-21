class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node):
    previous = None
    while node:
        previous = node
        node = node.next
    while previous:
        print(node.value)
        previous = node.prev
