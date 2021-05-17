# Сортировка пузырьком


def bubble_sort(nums):
    sort = False
    count = True
    while count:
        count = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                count = True
                sort = True
        if count:
            print(*nums)
    if not sort:
        print(*nums)


if __name__ == '__main__':
    with open('input.txt') as f:
        n = f.readline()
        nums = list(map(int, f.readline().strip().split()))
        bubble_sort(nums)
