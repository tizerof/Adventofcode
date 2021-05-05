# 51202141

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()


if __name__ == '__main__':
    s = Stack()
    with open('input.txt') as f:
        comands = f.readline().strip().split()
        for c in comands:
            try:
                s.push(int(c))
            except:
                a = s.pop()
                b = s.pop()
                case = {
                    '+': lambda a, b: b + a,
                    '-': lambda a, b: b - a,
                    '*': lambda a, b: b * a,
                    '/': lambda a, b: b // a,
                }
                s.push(case[c](a, b))
    print(s.pop())
