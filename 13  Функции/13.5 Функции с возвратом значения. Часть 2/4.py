# объявление функции
def is_password_good(password):
    upp = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, upp, low, dig])


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
