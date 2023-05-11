n=int(input())
a=['#','$','%','*']
b=4
c=0
for i in range(0,n):
    d=0
    for j in range(b):
        for k in range(c+1):
            print(a[d],end=' ')
        d=d+1
    c=c+1
    print('')
e=n-2
for i in range (n-1):
    f=0
    for j in range(b):
        for k in range(e+1):
            print(a[f],end=' ')
        f=f+1
    e=e-1
    print('')