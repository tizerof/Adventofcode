# На IT-конференции присутствовали студенты из разных вузов со всей страны.
# Для каждого студента известен ID университета, в котором он учится.
# Тимофей предложил Рите выяснить, из каких k вузов на конференцию пришло
# больше всего учащихся.

# Формат ввода
# В первой строке дано количество студентов в списке —– n(1 ≤ n ≤ 15 000)
# Во второй строке через пробел записаны n целых чисел —– ID вуза каждого
# студента. Каждое из чисел находится в диапазоне от 0 до 10 000.
# В третьей строке записано одно число k.

def students_count(students: list, universities: int) -> list:
    result = [0] * universities
    for s in students:
        university_id = int(s)
        if university_id <= universities:
            result[university_id - 1] += 1
    return [i[0]+1 for i in
            sorted(enumerate(result), reverse=True, key=lambda x: x[1])]


if __name__ == '__main__':
    with open('input.txt') as f:
        f.readline()
        students = f.readline().strip().split()
        university = int(f.readline())
        print(*students_count(students, university))
