n, m = (int(input()) for i in range(2))
matrix = [input().split() for line in range(n)]
for line in range(n):
    matrix[line].insert(0, '')
    matrix[line].append('')
empty_line = [''] * (m + 2)
matrix.insert(0, empty_line)
matrix.append(empty_line)
x, y = (int(input()) for i in range(2))
result = [
    matrix[x+1][y],
    matrix[x][y+1],
    matrix[x+2][y+1],
    matrix[x+1][y+2]
]
result = [int(i) for i in result if i != '']
print(' '.join(map(str, sorted(result))))
