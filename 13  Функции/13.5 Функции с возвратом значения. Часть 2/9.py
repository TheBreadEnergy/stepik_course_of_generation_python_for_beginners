# объявление функции
def convert_to_python_case(text):
    s = ''
    for el in text:
        if el.isupper():
            s += '_'
        s += el.lower()
    return s[1:]

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))