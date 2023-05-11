n,k=input().split(' ')
s=input().split(' ')
c,count=[],0
for i in range(0,len(s)):
    for j in range(i+1,len(s)): c.append([int(s[i]),int(s[j])])
for i in c:
    sum1=0
    sum1=i[0]+i[1]
    if(sum1%int(k)==0): count=count+1
print(count)
    