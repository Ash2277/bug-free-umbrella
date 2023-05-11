n = int(input())
l = []
for i in range(n):
    s = input()
    if len(s) <= 10:
        # print(s)
        l.append(s)
    else:
        a = str(len(s[1:-1]))
        out = s[0]+a+s[-1]
        # print(out)
        l.append(out)
for word in l:
    print(word)
