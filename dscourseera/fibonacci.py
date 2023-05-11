n = int(input())
a = [0, 1]
if(n == 0):
    print(a[0])
elif(n == 1):
    print(a[1])
else:
    for i in range(2, n+1):
        b = a[i-1]+a[i-2]
        a.append(b)
    print(a[-1])
