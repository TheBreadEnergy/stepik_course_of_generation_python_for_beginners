a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print('Равносторонний')
elif a==b!=c or b==c!=a or c==a!=b:
    print('Равнобедренный')
else:
    print('Разносторонний')