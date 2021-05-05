def fib(n, k):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, (a + b) % (10 ** k)
    return (a + b) % (10 ** k)


with open('input.txt') as f:
    n, k = tuple(map(int, f.readline().strip().split()))
    print(fib(n - 1, k))
