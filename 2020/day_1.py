def read_nums(file):
    """
    Reading a file with a list of numbers.
    """
    nums = []
    for line in f:
        nums.append(int(line))
    return nums


def sum_two_2020(nums):
    """
    Finds the multiplication of two digits
    from a list that sum to 2020
    """
    return [num*(2020-num) for num in nums if 2020 - num in nums][0]


def sum_three_2020(nums):
    """
    Finds the multiplication of three digits
    from a list that sum to 2020.
    """
    for i, num_1 in enumerate(nums):
        for num_2 in nums[i+1:]:
            if 2020 - num_1 - num_2 in nums:
                return (2020 - num_1 - num_2)*num_1*num_2


f = open('day_1.txt')
nums = read_nums(f)
print(sum_two_2020(nums))
print(sum_three_2020(nums))
