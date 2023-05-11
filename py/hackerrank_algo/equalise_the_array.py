n=int(input())
a=input().split(' ')
b,c=[],0
for i in a:
    if i not in b: b.append(i)
for i in b: 
    temp=int(a.count(i))
    if(temp>c): c=int(temp)
print(len(a)-c)