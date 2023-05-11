bud,n,m=input().split(' ')
a=input().split(' ')
b=input().split(' ')
c,d=[],[]
for i in a:
    for j in b: c.append([int(i),int(j)])
for i in c: 
    if(sum(i)<=int(bud)): d.append(sum(i))
if not (len(d)==0): print(max(d))
else: print(-1)