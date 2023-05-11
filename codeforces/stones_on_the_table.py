n = int(input())
stones = list(input())
count = 0
l1 = [stones[0]]
for i in range(1, n):
    if(stones[i-1] == stones[i]):
        count += 1
    if(stones[i-1] != stones[i]):
        l1.append(stones[i])
print(l1)
print(count)
