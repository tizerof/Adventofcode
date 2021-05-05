# Любимый вариант очереди Тимофея — очередь, написанная с использованием
# связного списка. Помогите ему с реализацией. Очередь должна поддерживать
# выполнение трёх команд:

# get() — вывести элемент, находящийся в голове очереди, и удалить его.
# Если очередь пуста, то вывести «error».
# put(x) — добавить число x в очередь
# size() — вывести текущий размер очереди

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def put(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def get(self):
        if self.is_empty():
            return 'error'
        else:
            result = self.head
            if self.size == 1:
                self.head = self.tail = None
                self.size = 0
                return result
            self.head = self.head.next
            self.size -= 1
            return result


with open('input.txt') as f:
    comads = int(f.readline())
    q = LinkedQueue()
    for i in range(comads):
        comand = f.readline().strip().split()
        if comand[0] == 'put':
            q.put(int(comand[1]))
        elif comand[0] == 'get':
            print(q.get())
        elif comand[0] == 'size':
            print(q.size)
