n = int(input())
i = 2
result = []
while i * i <= n:
    while n % i == 0:
        result.append(i)
        n = n / i
    i = i + 1
if n > 1:
    result.append(int(n))
print(*result)
