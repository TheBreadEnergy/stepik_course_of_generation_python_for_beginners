n = input()
p = 0
s = 0
for i in range(len(n)):
    if n[i].lower() in 'ауоыиэяюёе':
        p += 1
    elif n[i].lower() in 'бвгджзйклмнпрстфхцчшщ':
        s += 1
print('Количество гласных букв равно', p)
print('Количество согласных букв равно', s)