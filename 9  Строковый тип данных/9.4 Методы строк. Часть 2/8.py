s = input()
first = s.find('h')
last = s.rfind('h')
s = s[:first] + s[(last + 1):]
print(s)