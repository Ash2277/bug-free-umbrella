n = int(input())
s = 1
a = [0, 1]
if(n == 0):
    print('0')
elif(n == 1):
    print('1')
elif(n >= 1000000000):
    print(0)
else:
    for i in range(2, n+1):
        b = a[i-1]+a[i-2]
        a.append(b)
        s = s+(b*b)
    s = str(s)
    print(s[-1])
