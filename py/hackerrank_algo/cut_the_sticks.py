n=int(input())
a=list(map(int, input().strip().split(' ')))
print(len(a))
while(a):
    c,b=[],min(a)
    for i in a:
        if not(i-b==0): c.append(i-b)
    if not(len(c)==0):print(len(c))
    a=c