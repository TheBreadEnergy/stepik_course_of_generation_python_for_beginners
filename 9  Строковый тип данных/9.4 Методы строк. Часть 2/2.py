s = input().upper()
gen = "Аденин Гуанин Цитозин Тимин".split(" ")
for i in range(len(gen)):
    print(gen[i] + ":", s.count(gen[i][0:1]))