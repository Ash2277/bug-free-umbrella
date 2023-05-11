n=int(input())
a=str(input()).split(' ')
b=str(input()).split(' ')
sum1=0
sum2=0
for i in range(n):
    if(i%2==1):
        sum1=sum1+int(b[i])
        sum2=sum2+int(a[i])
    elif(i%2==0):
        sum1=sum1+int(a[i])
        sum2=sum2+int(b[i])
if(sum1>sum2):
    print(sum2)
else:
    print(sum1)