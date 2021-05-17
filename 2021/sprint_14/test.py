def merge(array, left, mid, right):
    left_part = array[left:mid]
    right_part = array[mid:right]
    k = left
    i = 0
    j = 0
    while (left + i < mid and mid + j < right):
        if (left_part[i] <= right_part[j]):
            array[k] = left_part[i]
            i += 1
        else:
            array[k] = right_part[j]
            j += 1
        k += 1
    if left + i < mid:
        while k < right:
            array[k] = left_part[i]
            i += 1
            k += 1
    else:
        while k < right:
            array[k] = right_part[j]
            j += 1
            k += 1
    return array


def merge_sort(array, left, right):
    if right - left > 1:
        mid = (left + right)//2
        merge_sort(array, left, mid)
        merge_sort(array, mid, right)
        merge(array, left, mid, right)


arr = [4, 5, 3, 0, 1, 2]
merge_sort(arr, 0, 4)
print(arr)
