# На клавиатуре старых мобильных телефонов каждой цифре соответствовало
# несколько букв.
# Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов.
# Напечатайте все комбинации букв, которые можно набрать такой
# последовательностью нажатий.

phone = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def gen_letters(nums, n=0, prefix=''):
    result = ''
    if n == len(nums):
        return prefix
    else:
        for letter in phone[nums[n]]:
            comb = gen_letters(nums, n + 1, prefix + letter)
            result += comb + ' '
    return result[:-1]


with open('input.txt') as f:
    nums = f.readline()
    print(gen_letters(nums))
