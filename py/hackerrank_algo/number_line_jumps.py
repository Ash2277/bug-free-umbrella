a=input().split(' ')
x1,v1,x2,v2=int(a[0]),int(a[1]),int(a[2]),int(a[3])
sum1,sum2=x1,x2
if(x2>x1 and v2>v1): print("NO")
elif(v1==v2): print('NO')
else:
    while(True):
        if(x1<x2):
            sum1=sum1+v1
            sum2=sum2+v2
            if(sum1==sum2):
                print('YES')
                exit()
            elif(sum1>sum2):
                print('NO')
                exit()
        elif(x2<x1):
            sum1=sum1+v1
            sum2=sum2+v2
            if(sum1==sum2):
                print('YES')
                exit()
            elif(sum2>sum1):
                print('NO')
                exit()
                