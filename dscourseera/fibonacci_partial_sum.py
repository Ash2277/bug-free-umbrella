m, n = map(int, input().split(' '))
a = [0, 1]
if(n == 0):
    print('0')
elif(n == 1):
    print('1')
else:
    for i in range(2, n+1):
        b = a[i-1]+a[i-2]
        a.append(b)
    c = a[m:]
    s = str(sum(c))
    print(s[-1])
