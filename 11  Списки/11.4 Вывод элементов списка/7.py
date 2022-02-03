n = int(input())
x = [int(input()) for _ in range(n)]
[print(i) for i in x if i < 0]
[print(i) for i in x if i == 0]
[print(i) for i in x if i > 0]