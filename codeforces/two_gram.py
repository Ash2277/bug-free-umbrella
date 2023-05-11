n = int(input())
s = input()
li = []
for i in range(1, n):
    li.append(s[i-1:i+1])
# print(li)
li2 = []
for i in li:
    if i not in li2:
        li2.append(i)
co = 0
out = ''
for i in li2:
    co1 = li.count(i)
    if co1 > co:
        co = co1
        out = i
print(out)
