n=int(input())
s=str(input())
a=s.split()
b=[]
sum1=0
if(n>0 and n<100):
    for i in a:
        sum1=sum1+int(i)
        if(int(i)%2==0):
            b.append(int(i)-15)
        else:
            b.append(int(i)+10)
    sum2=sum(b)
    if(sum2>sum1):
        print("Make changes")
        print('%.2f'%float(sum2/n))
    else:
        print('Do not make changes')
        print('%.2f'%float(sum1/n))