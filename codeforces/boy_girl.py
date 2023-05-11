s = input()
a = ''
for i in s:
    if i not in a:
        a = a+i
if len(a) % 2 == 0:
    print("CHAT WITH HER!")
if len(a) % 2 == 1:
    print("IGNORE HIM!")
