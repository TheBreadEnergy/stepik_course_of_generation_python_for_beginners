n, a, b = int(input()), [], []
for i in range(n):
    a.append(input())
for i in a:
    if i not in b:
        b.append(i)
print(*b, sep='\n')