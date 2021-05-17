# Вася решил накопить денег на два одинаковых велосипеда — себе и сестре.
# У Васи есть копилка, в которую каждый день он может добавлять деньги(если,
# конечно, у него есть такая финансовая возможность). В процессе накопления
# Вася не вынимает деньги из копилки.

# У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке
# было денег в каждый из дней.

# Ваша задача — по заданной стоимости велосипеда определить

# первый день, в которой Вася смог бы купить один велосипед,
# и первый день, в который Вася смог бы купить два велосипеда.
# Подсказка: решение должно работать за O(log n).

def sell_bike(arr, cost, start, end):
    len_search = end - start + 1
    if len_search < 1:
        return -1
    mid = (start + end) // 2
    ind = arr[mid]
    if len_search == 1 and cost <= int(ind):
        return mid + 1
    if cost <= int(ind):
        return sell_bike(arr, cost, start, mid)
    else:
        return sell_bike(arr, cost, mid+1, end)


if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline())
        arr = f.readline().strip().split()
        cost = int(f.readline())
        print(sell_bike(arr, cost, 0, n-1), sell_bike(arr, cost+cost, 0, n-1))
