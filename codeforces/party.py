n=int(input())
li=[]
for i in range(n):
    li.append(int(input()))
val=max(li)
fin=[0]*(val+1)
minus=0
for i in range(n):
    if li[i]==-1:
        minus+=1
    
