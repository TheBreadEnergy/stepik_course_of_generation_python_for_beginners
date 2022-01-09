word = input()
flag_palindrom = True
i = 0
j = len(word) - 1
while i < j:
    if word[i] != word[j]:
        flag_palindrom = False
        break
    i += 1
    j -= 1
if flag_palindrom:
    print('YES')
else:
    print('NO')