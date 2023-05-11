n,k=input().split(' ')
a=input().split(' ')
b=[int(x) for x in a]
c=max(b)
if(c-int(k)>0): print(c-int(k))
else: print(0)
