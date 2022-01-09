n = input()
plus = 0
star = 0
for i in range(len(n)):
    if n[i] in '+':
        plus += 1
    if n[i] in '*':
        star += 1
print('Символ + встречается', plus, 'раз')
print('Символ * встречается', star, 'раз')