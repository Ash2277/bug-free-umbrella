s=input()
a=input().split(' ')
b=input().split(' ')
n=[int(x) for x in a]
m=[int(x) for x in b]
n.sort()
m.sort()
d,e=[],[]
for i in range(1,m[0]+1):
    count=0
    for j in n:
        if(i%j==0): count=count+1
    if(count==len(n)): d.append(i)
for i in d:
    count=0
    for j in m:
        if(j%i==0): count+=1
    if(count==len(m)): e.append(i)
print(len(e))
        