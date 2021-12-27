a, b = input(), input()
red = 'красный'
blue = 'синий'
y = 'желтый'
if a==b and (a==red or a==blue or a==y):
    print(a)
elif (a==red or b==red) and (a==blue or b==blue):
    print('фиолетовый')
elif (a==red or b==red) and (a==y or b==y):
    print('оранжевый')
elif (a==y or b==y) and (a==blue or b==blue):
    print('зеленый')
else:
    print('ошибка цвета')