# Сортировка слиянием

def merge(arr: list, left: int, mid: int, right: int) -> list:
    left_arr = arr[left:mid]
    right_arr = arr[mid:right]
    l, r, k = 0, 0, left
    while left + l < mid and mid + r < right:
        if left_arr[l] <= right_arr[r]:
            arr[k] = left_arr[l]
            l += 1
            k += 1
        else:
            arr[k] = right_arr[r]
            r += 1
            k += 1
    while l < len(left_arr):
        arr[k] = left_arr[l]
        l += 1
        k += 1
    while r < len(right_arr):
        arr[k] = right_arr[r]
        r += 1
        k += 1
    return arr


def merge_sort(arr: list, left: int, right: int):
    if right - left == 1:
        return arr
    mid = (left + right)//2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)
    merge(arr, left, mid, right)


if __name__ == '__main__':
    arr = [4, 5, 3, 0, 1, 2]
    merge_sort(arr, 0, 4)
    print(arr)
