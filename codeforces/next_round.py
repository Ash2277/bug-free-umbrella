n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
count = 0
score_check = int(a[int(k)-1])
for score in a:
    if score >= score_check and score != 0:
        count += 1
print(count)
