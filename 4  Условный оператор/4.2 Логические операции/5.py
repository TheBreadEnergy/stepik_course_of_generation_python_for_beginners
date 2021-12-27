a, b, c = int(input()), int(input()), int(input())

if (c < a + b) and (a < b + c) and (b < a + c):
    print('YES')
else:
    print('NO')