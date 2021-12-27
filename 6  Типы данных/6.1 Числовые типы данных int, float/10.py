n = int(input())

n1 = n//100
n2 = (n//10)%10
n3 = n%10

s = n1+n2+n3

if max(n1, n2, n3)-min(n1, n2, n3) == s-max(n1, n2, n3)-min(n1, n2, n3):
    print('Число интересное')
else:
    print('Число неинтересное')
