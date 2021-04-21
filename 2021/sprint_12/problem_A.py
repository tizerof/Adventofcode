# 50652481


def get_list_between_zeros(distance):
    """Отдает список ближайшего расстояния от начала или от конца. """
    if distance % 2 == 0:
        nums = range(1, distance // 2 + 1)
        return [*nums, *reversed(nums)]
    else:
        nums = range(1, (distance + 1) // 2 + 1)
        return [*nums, *reversed(nums[:-1])]


def near_zero(nums):
    """Находим расстояние до ближайшего нуля в списке. """
    zero_indexes = [i for i, x in enumerate(nums) if x == 0]
    # если в списке один ноль, то сразу выдаем список
    if len(zero_indexes) == 1:
        return [abs(zero_indexes[0] - i) for i in range(len(nums))]
    result = []
    # если ноль на первом месте, проставляем расстояния до следующего нуля
    if zero_indexes[0] == 0:
        result.append(0)
        result.extend(get_list_between_zeros(zero_indexes[1] - 1))
        result.append(0)
        zero_indexes.remove(0)
    else:
        result.extend(range(zero_indexes[0], -1, -1))
    # добавляем остальные расстояния
    for i in range(len(zero_indexes[:-1])):
        result.extend(get_list_between_zeros(
            zero_indexes[i+1]-zero_indexes[i] - 1))
        result.append(0)
    # если ноль не на последнем месте, добавляем расстояния до последних чисел
    if zero_indexes[-1] != len(nums) - 1:
        result.extend(range(1, len(nums)-zero_indexes[-1]))
    return result


def main():
    with open('input.txt') as f:
        f.readline()
        nums = list(map(int, f.readline().strip().split()))
        print(*near_zero(nums))


if __name__ == '__main__':
    import cProfile
    cProfile.run('main()')
