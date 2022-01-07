num = int(input())
n = num
size = 0
while num != 0:
    last_digit = num % 10
    size += 1
    num = num // 10
print(n % 10 ** (size - 1) // 10 ** (size - 2))
