# 51202746

class Dequeue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_front(self, x):
        if self.size != self.max_n:
            self.queue[self.head] = x
            self.head = (self.head - 1 + self.max_n) % self.max_n
            self.size += 1
        else:
            print('error')

    def push_back(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop_front(self):
        if self.is_empty():
            return 'error'
        num = (self.head + 1) % self.max_n
        x = self.queue[num]
        self.queue[num] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            return 'error'
        num = (self.tail - 1 + self.max_n) % self.max_n
        x = self.queue[num]
        self.queue[num] = None
        self.tail = (self.tail - 1 + self.max_n) % self.max_n
        self.size -= 1
        return x


if __name__ == '__main__':
    with open('input.txt') as f:
        comands = int(f.readline())
        d = Dequeue(int(f.readline()))
        for i in range(comands):
            comand = f.readline().strip().split()
            case = {
                'push_front': lambda x: d.push_front(int(x)),
                'push_back': lambda x: d.push_back((int(x))),
                'pop_front': lambda: d.pop_front(),
                'pop_back': lambda: d.pop_back(),
            }
            if comand[0].split('_')[0] == 'push':
                case[comand[0]](comand[1])
            else:
                print(case[comand[0]]())
