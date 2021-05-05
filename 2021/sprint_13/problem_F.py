class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        print('error')

    def get_max(self):
        if not self.items:
            return None
        return max(self.items)


s = Stack()
with open('input.txt') as f:
    for i in range(int(f.readline())):
        comand = f.readline().strip().split()
        if comand[0] == 'push':
            s.push(int(comand[1]))
        elif comand[0] == 'pop':
            s.pop()
        elif comand[0] == 'get_max':
            print(s.get_max())
