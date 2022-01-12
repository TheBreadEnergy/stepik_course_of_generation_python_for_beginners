n = int(input())
a = []
for _ in range(n):
    a.append(input())
index = int(input())
res = ''
for s in a:
    if len(s) >= index:
        res += s[index - 1]

print(res)