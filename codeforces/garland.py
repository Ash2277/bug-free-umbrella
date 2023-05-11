n = int(input())
out = []
for i in range(n):
    bulbs = input()
    li = []
    for i in bulbs:
        li.append(bulbs.count(i))
    li.sort()
    if li == [4, 4, 4, 4]:
        out.append(-1)
    if li == [1, 3, 3, 3]:
        out.append(6)
    if li == [1, 1, 2, 2] or li == [2, 2, 2, 2] or li == [1, 1, 1, 1]:
        out.append(4)
for i in out:
    print(i)
