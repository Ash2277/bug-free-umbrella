k = int(input())
s = list(map(int, input().split(' ')))
s.sort(reverse=True)
val = 0
count = 0
for i in s:
    if val < k:
        val += i
        count += 1
    else:
        break
print(count)
