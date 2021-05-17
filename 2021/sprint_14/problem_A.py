# Рита по поручению Тимофея наводит порядок в правильных скобочных
# последовательностях(ПСП), состоящих только из круглых скобок().
#  Для этого ей надо сгенерировать все ПСП длины 2n в алфавитном
# порядке —– алфавит состоит из(и) и открывающая скобка идёт раньше
#  закрывающей.

# Помогите Рите —– напишите программу, которая по заданному n выведет
# все ПСП в нужном порядке.

def gen_brack(pairs, search='', left=0, right=0):
    if left == pairs and right == pairs:
        print(search)
    else:
        if left < pairs:
            gen_brack(pairs, search + '(', left + 1, right)
        if right < left:
            gen_brack(pairs, search + ')', left, right + 1)


with open('input.txt') as f:
    x = int(f.readline())
    gen_brack(x)
