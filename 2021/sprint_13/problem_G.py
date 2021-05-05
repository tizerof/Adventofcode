# Реализуйте класс StackMaxEffective, поддерживающий операцию определения
# максимума среди элементов в стеке. Сложность операции должна быть O(1).
# Для пустого стека операция должна возвращать None. При этом push и pop
# также должны выполняться за константное время.

class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        self.items.append(item)
        if not self.max:
            self.max.append(item)
        elif item >= self.max[-1]:
            self.max.append(item)

    def pop(self):
        if self.items:
            item = self.items.pop()
            if id(self.max[-1]) == id(item):
                self.max.pop()
        else:
            print('error')

    def get_max(self):
        if self.max:
            return self.max[-1]
        return None


s = StackMaxEffective()
with open('input.txt') as f:
    for i in range(int(f.readline())):
        comand = f.readline().strip().split()
        if comand[0] == 'push':
            s.push(int(comand[1]))
        elif comand[0] == 'pop':
            s.pop()
        elif comand[0] == 'get_max':
            print(s.get_max())
