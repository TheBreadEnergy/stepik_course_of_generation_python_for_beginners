n1, n2, n3, n4 = int(input()), int(input()), int(input()), int(input())

if abs(n1 - n3) <= 1 and abs(n2 - n4) <= 1:
    print('YES')
else:
    print('NO')