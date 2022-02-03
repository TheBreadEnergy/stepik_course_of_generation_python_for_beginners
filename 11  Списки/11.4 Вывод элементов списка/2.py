n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(*a, sep='\n')
print()
for i in a:
    print(i**2+2*i+1)