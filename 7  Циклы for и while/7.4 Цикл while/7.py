n = int(input())
m = 0
while n != 0:
    if n - 25 >= 0:
        n -= 25
        m += 1
    elif n - 10 >= 0:
        n -= 10
        m += 1
    elif n - 5 >= 0:
        n -= 5
        m += 1
    elif n - 1 >= 0:
        n -= 1
        m += 1
print(m)
