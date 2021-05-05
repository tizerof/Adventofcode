def transpose(y, nums):
    for j in range(y):
        new_line = []
        for line in nums:
            new_line.append(line[j])
        print(*new_line)


with open('input.txt') as f:
    f.readline()
    y = int(f.readline())
    nums = [i.split() for i in f.read().strip().split('\n')]
    print(nums)
    transpose(y, nums)
