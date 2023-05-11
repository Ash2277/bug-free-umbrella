#online
# q=int(input())
# x,y,z=[],[],[]
# for i in range(q):
#     a,b,c=input().split(' ')
#     x.append(int(a))
#     y.append(int(b))
#     z.append(int(c))
# if abs(x - z) < abs(y - z):
#         print('Cat A')
# elif abs(x - z) > abs(y - z):
#         print('Cat B')
# else:
#         print('Mouse C')
#my code
q=int(input())
x,y,z=[],[],[]
for i in range(q):
    a,b,c=input().split(' ')
    x.append(int(a))
    y.append(int(b))
    z.append(int(c))
for i in range(q):
    count1,count2=0,0
    while(z[i]!=x[i] or z[i]!=y[i]):
        if(x[i]<z[i]): x[i],count1=x[i]+1,count1+1
        elif(x[i]>z[i]): x[i],count1=x[i]-1,count1+1
        if(y[i]<z[i]): y[i],count2=y[i]+1,count2+1
        elif(y[i]>z[i]): y[i],count2=y[i]-1,count2+1
    if(count1<count2): print('Cat A')
    elif(count1>count2): print('Cat B')
    elif(count1==count2): print('Mouse C')