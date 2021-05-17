# Вечером ребята решили поиграть в игру «Большое число».
# Даны числа. Нужно определить,
# какое самое большое число можно из них составить.


def sort(nums):
    count = True
    while count:
        count = False
        for i in range(len(nums)-1):
            if int(nums[i]+nums[i+1]) < int(nums[i+1]+nums[i]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
                count = True
    return nums


if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline())
        nums = f.readline().strip().split()
        print(''.join(sort(nums)))
