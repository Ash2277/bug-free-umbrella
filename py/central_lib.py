n=int(input())
a=input()
b=a.split(' ')
c=[]
count=0
for i in b:
    sum1=0
    for j in range(len(i)):
        sum1=sum1+int(i[j])
    c.append(sum1)
d=[]
for i in c:
    if i not in d:
        d.append(i)
for i in d:
    count+=1
print(count)