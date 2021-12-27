year = int(input())

n1 = (year//10)%10
n2 = year%10

if n1==0 and n2==0:
    print('YES')
else:
    print('NO')