n=input()
s=str(input())
a=s.split(' ')
b=[int(x) for x in a]
b.sort()
b.reverse()
c=[x for x in b if x==b[0]]
print(len(c))