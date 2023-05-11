n=int(input())
l1=[]
l2=[]
l3=[]
for i in range(n):
    in1,in2,in3=map(int,input().split(' '))
    l1.append(in1)
    l2.append(in2)
    l3.append(in3)
out1=sum(l1)
out2=sum(l2)
out3=sum(l3)
if out1==0 and out2==0 and out3==0:
    print('YES')
else:
    print('NO')
