n,k=map(int,input().split())
while k>0:
    b=str(n)
    if b[-1]!='0':
        n-=1
    if b[-1]=='0':
        n=int(n/10)
    k-=1
print(n)