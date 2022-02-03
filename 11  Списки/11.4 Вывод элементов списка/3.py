n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in a:
    if i != max(a) and i != min(a):
        print(i)