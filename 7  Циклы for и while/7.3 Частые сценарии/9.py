n = int(input())

n1 = int(input())
n2 = int(input())

for _ in range(n-2):
    i = int(input())
    if i > n1:
        if i > n2:
            n2, n1 = n1, i
        else:
            n1 = i
    elif i > n2:
        n2 = i


print(max(n1, n2))
print(min(n1, n2))