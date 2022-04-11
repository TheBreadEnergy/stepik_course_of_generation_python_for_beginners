numbers = [int(i) for i in input().split()]
Max = numbers.index(max(numbers))
Min = numbers.index(min(numbers))
numbers[Max], numbers[Min] = min(numbers), max(numbers)
print(*numbers)