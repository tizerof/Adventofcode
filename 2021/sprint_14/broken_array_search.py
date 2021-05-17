# 51394337

def left_right_search(arr: list, left: int, right: int) -> tuple:
    """ Находим позиции крайних элементов основного массива. """
    if right - left <= 1:
        return left, right
    mid = (left + right) // 2
    if int(arr[mid]) < int(arr[right]):
        return left_right_search(arr, left, mid)
    else:
        return left_right_search(arr, mid, right)


def binarySearch(arr: list, k: int, left: int, right: int) -> int:
    """Бинарный поиск."""
    mid = (left + right) // 2
    mid_num = int(arr[mid])
    if mid_num == k:
        return mid
    if right <= left:
        return -1
    elif k < mid_num:
        return binarySearch(arr, k, left, mid)
    else:
        return binarySearch(arr, k, mid + 1, right)


def broken_array_search(arr: list, n: int, k: int) -> int:
    right, left = left_right_search(arr, 0, n-1)
    i = binarySearch(arr[left:]+arr[:right+1], k, 0, n-1)
    if i >= 0:
        return (i + right + 1) % n
    return i


if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline())
        k = int(f.readline())
        arr = f.readline().strip().split()
        print(broken_array_search(arr, n, k))
