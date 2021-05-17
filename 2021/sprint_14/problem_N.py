# Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам.
# На схеме земельного участка клумбы обозначаются просто горизонтальными
# отрезками, лежащими на одной прямой. Для ландшафтных работ было нанято
# n садовников. Каждый из них обрабатывал какой-то отрезок на схеме.
# Процесс был организован не очень хорошо, иногда один и тот же отрезок
# или его часть могли быть обработаны сразу несколькими садовниками.
# Таким образом, отрезки, обрабатываемые двумя разными садовниками,
# сливаются в один. Непрерывный обработанный отрезок затем станет клумбой.
# Нужно определить границы будущих клумб.

def garden(segments, n):
    segments = sorted(
        segments, key=lambda x: [x[0], -x[1]])
    result = [segments[0]]
    r = 0
    s = 1
    while s < n:
        if segments[s][0] <= result[r][1]:
            result[r][1] = max(segments[s][1], result[r][1])
        else:
            result.append(segments[s])
            r += 1
        s += 1
    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline())
        segments = [list(map(int, f.readline().strip().split()))
                    for i in range(n)]
        for line in garden(segments, n):
            print(*line)
