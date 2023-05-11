import math
n=int(input())
b=[str(input()) for i in range(n)]
d=[x.split(" ") for x in b]
a=[int(d[x][x]) for x in range(n)]
sum1=sum(a)
e,f,sum2=n-1,0,0
while(e>=0):
    sum2=sum2+int(d[f][e])
    e=e-1
    f=f+1
print(abs(sum1-sum2))