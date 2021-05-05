from typing import List, Iterator


# 1. Что делает, как работает
# 2. Проблемы
def test0(a):
    if a > 0:
        return test0(a - 1)
    return a


# 1. Что произойдёт при запуске
# 2. Что вернёт
def test1():
    return list(map(lambda x: print(x), range(10)))


# Как работает? Что вернёт?
def test2() -> List[int]:
    def func(a: int):
        for i in range(a):
            yield i
        yield a
    a = func(7)
    return list(a)

# Что напишет? Почему?


def test3():
    a = 7
    print(id(7) == id(a))
    b = 555
    print(id(b) == id(555))
    c = '123'
    print(id(c) == id('123'))


def test4():
    a = {}
    _id = id(a)
    a = {}
    a['test'] = 123
    return id(a) == _id


# Что произойдёт при запуске?
def test5():
    test_value = 3

    def local_func(value):
        print(value)
        value += 3
        yield value
        value += 3
        yield value
    list(local_func(test_value))
    local_func()


# Что вернёт?
def test6():
    test_t = ([1, 2, 3, 4],)
    test_t[0].append(5)
    return test_t

# Что это?


def test7(func):
    def wrapper():
        func()
    return wrapper


# Что может быть ключом словаря?
def test8():
    a = {}
    a[None] = 13333
    a[True] = 2
    a[1] = 1
    a['1'] = '1'
    a[(1, '1')] = (1, '1')
    a[0b001001] = 9
    return a


# Что вернёт?
def test9():
    def func(a=[]):
        a.append('b')
        return a
    b = func()
    c = func()
    d = func([])
    return b, c, d


# print(test0(5))
# print(test1())
# print(test2())
# print(test3())
# print(test4())
# print(test5())
# print(test6())
# print(test7())
# print(test8())
# print(test9())

# Задание: Написать функцию валидатор IP


def valid_ip(adr: str):
    def funk(x):
        print('"', x, '"')
        if x.isnumeric():
            return True if 0 <= int(x) < 256 else False
        return False
    adr_list = [funk(num) for num in adr.split('.')]
    return all(adr_list)


test = (
    '192.168.0.1',
    'test',
    'test.test.test.test',
    '300.500.0.1',
    '192.16+8.0.1'
)
for i in test:
    print(valid_ip(i))
