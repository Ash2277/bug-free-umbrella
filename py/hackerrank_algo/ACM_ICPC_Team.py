from itertools import permutations
n, m = map(int, input().strip().split(" "))
a, c, b = [], [], ''
for i in range(m):
    b = b+'1'
for i in range(n):
    a.append(i+1)
    c.append(input())
perm = permutations(a)
print(perm)
