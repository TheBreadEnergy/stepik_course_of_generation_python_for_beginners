# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, i):
#         print('*', end='')
#     print()
# for i in range(n-1, 1, -1):
#     for j in range(1, i):
#         print('*', end='')
#     print()

n = int(input())
for i in range(1, n + 1):
    print('*' * min(i, n - i + 1))