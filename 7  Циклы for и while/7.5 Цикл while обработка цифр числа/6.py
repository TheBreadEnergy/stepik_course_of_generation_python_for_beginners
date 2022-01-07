num = int(input())
check = True
last = num % 10
while num != 0:
    last_digit = num % 10
    if last_digit != last:
        check = False
        break
    num = num // 10

if check:
    print('YES')
else:
    print('NO')
