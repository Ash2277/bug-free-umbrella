n = int(input())
counter = 0
for i in range(n):
    a = input().split(' ')
    if(a.count('1') > 1):
        counter += 1
print(counter)
