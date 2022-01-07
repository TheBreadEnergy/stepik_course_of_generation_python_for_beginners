num = int(input())
max = num % 10
min = num % 10
while num != 0:
    last_digit = num % 10
    if last_digit > max:
        max = last_digit
    if last_digit < min:
        min = last_digit
    num = num // 10
print('Максимальная цифра равна', max)
print('Минимальная цифра равна', min)