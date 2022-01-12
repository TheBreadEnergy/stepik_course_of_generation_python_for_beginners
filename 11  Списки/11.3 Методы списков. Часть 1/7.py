n, c = int(input()), int(input())
a = []
for _ in range(n-1):
    b = int(input())
    a.append(c + b)
    c = b
print(a)