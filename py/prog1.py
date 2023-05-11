t=int(input())
a=[]
for i in range(t):
    b=input().split(' ')
    c=[int(x) for x in b]
    a.append(c)
for i in a:
    count=0
    d=abs(i[0]-i[1])
    if(i[0]==i[1]):
        print('0 0')
    elif(d==1):
        if(i[0]==1 or i[1]==1):
            print('1 0')
        elif(i[0]>i[1]):
            print('1',i[1])
        elif(i[0]<i[1]):
            print('1',i[0])
    elif(i[0]%d==1 and i[1]%d==1):
        print(d,1)
    else:
        while(i[0]%d!=0 and i[1]%d!=0):
            i[0]+=1
            i[1]+=1
            count+=1
        print(d,count)



        