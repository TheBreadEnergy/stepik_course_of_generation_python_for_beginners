# объявление функции
def draw_triangle():
    print(*['*' * i for i in range(1, 11)], sep='\n')

# основная программа
draw_triangle()  # вызов функции