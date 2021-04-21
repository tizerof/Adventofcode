s = sorted(input())
t = sorted(input())
result = ''
for i in range(len(s)):
    if s[i] != t[i]:
        result = t[i]
        break
if result:
    print(result)
else:
    print(t[-1])
