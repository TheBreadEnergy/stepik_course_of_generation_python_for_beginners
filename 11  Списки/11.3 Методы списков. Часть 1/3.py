a = []
for i in range(ord('z') - ord('a') + 1):
    a.append(chr(ord('a') + i) * (i + 1))
print(a)