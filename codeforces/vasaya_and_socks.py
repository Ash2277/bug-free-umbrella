n, m = map(int, input().split(' '))
count = 0
while(n != 0):
    n = n-1
    count += 1
    if(count % m == 0):
        n += 1
print(count)
