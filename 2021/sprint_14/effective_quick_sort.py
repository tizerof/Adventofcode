# 51411982

def partition(array: list, left: int, right: int) -> int:
    """ Сортируем элементы в массиве, слева меньше pivot, справа больше."""
    pivot = (left + right) // 2
    array[left], array[pivot] = array[pivot], array[left]
    pivot = left
    while right >= left:
        while left <= right and array[left] <= array[pivot]:
            left += 1
        while left <= right and array[right] > array[pivot]:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        else:
            break
    array[pivot], array[right] = array[right], array[pivot]
    return right


def quicksort(array: list, left: int, right: int):
    """ Быстрая эффективная сортировка."""
    if left >= right:
        return
    if right - left <= 1:
        if array[right] < array[left]:
            array[right], array[left] = array[left], array[right]
            return
    mid = partition(array, left, right)
    quicksort(array, left, mid - 1)
    quicksort(array, mid + 1, right)


if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline())
        participants = [()] * n
        for i in range(n):
            line = f.readline().strip().split()
            participants[i] = ((-int(line[1]), int(line[2]), line[0]))
        quicksort(participants, 0, n-1)
        for part in participants:
            print(part[2])
