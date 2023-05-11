n, m = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
a.sort()
val = 0
# print(a)
for i in range(m):
    if a[i] <= 0:
        val += abs(a[i])
    else:
        break
print(val)
