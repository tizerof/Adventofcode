# Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов.
# Если вы с ней ещё не сталкивались, то наверняка столкнётесь –— она довольно
# популярная.

# Дана скобочная последовательность. Нужно определить, правильная ли она.

# Будем придерживаться такого определения:

# пустая строка —– правильная скобочная последовательность
# правильная скобочная последовательность, взятая в скобки одного типа, –—
# правильная скобочная последовательность
# правильная скобочная последовательность с приписанной слева или справа
# правильной скобочной последовательностью —– тоже правильная.
# На вход подается последовательность из скобок трёх видов: [], (), {}.
# Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную
# последовательность и возвращает True, если последовательность правильная,
# а иначе False.


from os import error


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return False

    def is_empty(self):
        if self.items[:1]:
            return False
        return True


def is_correct_bracket_seq(line):
    brackets = ['[]', '()', '{}', ]
    brackets_open = [x[0] for x in brackets]
    brackets_partner = {x[1]: x[0] for x in brackets}
    s = Stack()
    for c in line:
        if c in brackets_open:
            s.push(c)
        elif c in brackets_partner:
            last = s.pop()
            if last != brackets_partner[c]:
                return False
    return s.is_empty()


with open('input.txt') as f:
    print(is_correct_bracket_seq(f.read().strip()))
