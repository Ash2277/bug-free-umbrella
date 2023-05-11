l = "qwertyuiopasdfghjkl;zxcvbnm,./"
pos = input()
s = input()
out = ''
if pos == 'R':
    for i in s:
        ind = l.index(i)
        # print(ind)
        out += l[ind-1]
if pos == 'L':
    for i in s:
        ind = l.index(i)
        out += l[ind+1]
print(out)
