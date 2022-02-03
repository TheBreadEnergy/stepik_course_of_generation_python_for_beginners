a = [input() for _ in range(int(input()))]
b = [input() for _ in range(int(input()))]
for i in a:
    for j in b:
        if j.lower() not in i.lower():
            break
    else:
        print(i)