def quick_merge(n):
    return sorted([int(i) for i in range(n) for i in input().split()])


n = int(input())

print(*quick_merge(n))
