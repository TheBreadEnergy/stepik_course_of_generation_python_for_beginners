n = int(input())
a = 0
for i in range(n):
    s = input()
    if s.count('11') >= 3:
        a = a + 1
print(a)