num = int(input())
last = num % 10
quantity = 0
sum = 0
prod = 1
while num != 0:
    last_digit = num % 10
    quantity += 1
    sum += last_digit
    prod *= last_digit
    num = num // 10
print(sum)
print(quantity)
print(prod)
print(sum / quantity)
print(last_digit)
print(last + last_digit)
