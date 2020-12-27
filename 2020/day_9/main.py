# https://adventofcode.com/2020/day/9


def is_num_sum_of_two_in_nums(num,nums):
    """
    Checks if a number is the sum of two
    numbers in the list of numbers.
    """
    buffer_nums = ()
    for num1 in nums:
        if num1 in buffer_nums:
            return True
        buffer_nums += (num - num1,)
    return False


def encrypting_XMAS():
    """
    Finds a number in a file that is not
    the sum of the two previous 25 numbers.
    """
    last_nums = []
    for line in open("input.txt").read().splitlines():
        if len(last_nums) < 26:
            last_nums.append(int(line))
            continue
        if is_num_sum_of_two_in_nums(int(line), last_nums):
            last_nums.pop(0)
            last_nums.append(int(line))
        else:
            return int(line)
    return 0


def encrypting_XMAS_second():
    """
    Finds a list of numbers in a file that come before an invalid number.
    Their sum is equal to the wrong number. Time complexity is O(n).
    """
    invalid_number = encrypting_XMAS()
    nums = [int(line) for line in open("input.txt").read().splitlines()]
    start = 0
    end = 1
    nums_sum = nums[0] + nums[1]
    while True:
        if nums_sum < invalid_number:
            end = end + 1
            nums_sum = nums_sum + nums[end]
        if nums_sum > invalid_number:
            nums_sum = nums_sum - nums[start]
            start = start + 1
        if nums_sum == invalid_number:
            answer = nums[start:end+1]
            return min(answer) + max(answer)


print(encrypting_XMAS())
print(encrypting_XMAS_second())