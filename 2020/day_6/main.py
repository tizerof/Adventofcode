# https://adventofcode.com/2020/day/6


def count_questions(file_name):
    return sum([len(set(group.replace("\n", ""))) for group in open(file_name).read().split('\n\n')])


def count_questions_second(file_name):
    return sum([sum([1 for question in set(group.replace("\n", "")) 
                     if group.count(question) == group.count("\n")+1]) 
                for group in open(file_name).read().split('\n\n')])


print(count_questions("input.txt"))
print(count_questions_second("input.txt"))