a = []
for _ in range(int(input())):
    a.append(int(input()))
del a[1::2]
print(a)