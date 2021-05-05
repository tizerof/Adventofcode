# Астрологи объявили день очередей ограниченного размера. Тимофею нужно написать
# класс MyQueueSized, который принимает параметр max_size, означающий максимально
# допустимое количество элементов в очереди.

# Помогите ему —– реализуйте программу, которая будет эмулировать работу такой
# очереди. Функции, которые надо поддержать, описаны в формате ввода.

class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.siz = 0

    def is_empty(self):
        return self.siz == 0

    def push(self, x):
        if self.siz != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.siz += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.siz -= 1
        return x

    def peek(self):
        return self.queue[self.head]

    def size(self):
        return self.siz


with open('input.txt') as f:
    comads = int(f.readline())
    q = MyQueueSized(int(f.readline()))
    for i in range(comads):
        comand = f.readline().strip().split()
        if comand[0] == 'push':
            q.push(int(comand[1]))
        elif comand[0] == 'pop':
            print(q.pop())
        elif comand[0] == 'peek':
            print(q.peek())
        elif comand[0] == 'size':
            print(q.size())
