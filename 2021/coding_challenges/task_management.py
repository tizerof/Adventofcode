from itertools import combinations
from time import time


def first(n, k, l, m):
    return sum(1 for task in range(1, n+1)
               if (task % k) and (task % l) and (task % m))


def second(n, k, l, m):
    count = 0
    for task in range(1, n+1):
        if (task % k) and (task % l) and (task % m):
            count += 1
    return count


def tasks_done(n: int, k: int, i: int, m: int) -> int:
    result = n
    unique_chill = {k, i, m}  # использую множество
    for chill in unique_chill:
        result -= n // chill
    return result


def tasks_in_day(n, k, l, m):
    """Находим количество выполненных тасков в день. """
    skip_tasks = sorted([k, l, m])
    dividers_counter = 0
    # Проверяем есть ли делители в введенных данных.
    # Если есть, меняем номер пропускаемого таска на n.
    if (skip_tasks[2] % skip_tasks[1] == 0
            or skip_tasks[2] % skip_tasks[0] == 0):
        skip_tasks[2] = n
        dividers_counter += 1
    if skip_tasks[1] % skip_tasks[0] == 0:
        skip_tasks[1] = n
        dividers_counter += 1
    exclude = sum(n // i for i in skip_tasks)   # все пропущенные таски
    reiterations = sum(n // (i[0] * i[1])       # повторы пропусков
                       for i in list(combinations(skip_tasks, 2)))
    extra = n // (skip_tasks[0] * skip_tasks[1] * skip_tasks[2])
    # Вычитаем из n количество пропущенных тасков.
    return n - exclude + reiterations - extra + dividers_counter


def main():
    with open('input.txt') as f:
        n, k, l, m = map(int, f.readline().strip().split())
        print(list(range(1, n+1)))
        print(tasks_in_day(n, k, l, m))
        print(tasks_done(n, k, l, m))


if __name__ == '__main__':
    now = time()
    main()
    print(time() - now)
