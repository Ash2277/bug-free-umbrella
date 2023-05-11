n=str(input())
a=n.split(' ')
b=[int(x) for x in a]
b.sort()
min=sum(b[0:4])
print(min,end=' ')
max=sum(b[1:5])
print(max)