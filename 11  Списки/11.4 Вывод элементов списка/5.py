n, a = int(input()), []
for i in range(n):
    a.append(input())
k = input()
for i in a:
    if k.lower() in i.lower():
        print(i)