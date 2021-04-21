# Вася размышляет, что бы такое из списка не делать. Но, кажется, все пункты
# очень важные! Вася решает загадать число и удалить дело, которое идёт под
# этим номером. Список дел представлен в виде односвязного списка. Напишите
# функцию solution, которая принимает на вход голову списка и номер удаляемого
# дела и возвращает голову обновлённого списка.
# Внимание: в этой задаче не нужно считывать входные данные. Нужно написать
# только функцию, которая принимает на вход голову списка и номер удаляемого
# элемента и возвращает голову обновленного списка. Ниже дано описание структуры,
# которая задаёт вершину списка.


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def print_list(vertex):
    while vertex:
        print(vertex.value)
        vertex = vertex.next_item


def solution(vertex, idx):
    count = 0
    if idx == 0:
        return vertex.next_item
    node = vertex
    while node:
        if count + 1 == idx:
            node.next_item = node.next_item.next_item
            break
        node = node.next_item
        count += 1
    return vertex


n6 = Node('6')
n5 = Node('5', n6)
n4 = Node('4', n5)
n3 = Node('3', n4)
n2 = Node('2', n3)
n1 = Node('1', n2)
print_list(solution(n1, 2))
