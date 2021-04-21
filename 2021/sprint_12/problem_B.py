# 50670324

def sleight_of_hand(k, nums):
    """Перебираем числа от 1 до 9 и проверяем
    получится ли нажать на все клавиши с этими числами. """
    result = 0
    for t in range(10):
        count = nums.count(str(t))
        if 0 < count <= int(k) * 2:
            result += 1
    return result


def main():
    with open('input.txt') as f:
        k = f.readline()
        nums = f.read()
        print(sleight_of_hand(k, nums))


if __name__ == '__main__':
    main()
