n1=str(input())
n2=str(input())
c1=0
c2=0
for i in n1:
    if(i.isupper()==True):
        c1+=1
for j in n2:
    if(j.isupper()==True):
        c2+=1
if(c1==c2 and (c1!=0 or c2!=0)):
    print(1)
else:
    print(0)