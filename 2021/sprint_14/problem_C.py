# Гоша любит играть в игру «Подпоследовательность»: даны 2 строки, и нужно
# понять, является ли первая из них подпоследовательностью второй.
# Когда строки достаточно длинные, очень трудно получить ответ на
# этот вопрос, просто посмотрев на них. Помогите Гоше написать функцию,
# которая решает эту задачу.

def is_subseq(first_seq, second_seq):
    i = j = 0
    f_len, s_len = len(first_seq), len(second_seq)
    while i < f_len and j < s_len:
        if first_seq[i] == second_seq[j]:
            i += 1
        j += 1
    return i == f_len


if __name__ == '__main__':
    with open('input.txt') as f:
        first_seq = f.readline().strip()
        second_seq = f.readline().strip()
        print(is_subseq(first_seq, second_seq))
