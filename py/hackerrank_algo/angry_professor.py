n=int(input())
for i in range(n):
    n,k=input().split(' ')
    a=input().split(' ')
    count=0
    for i in a:
        if(int(i)<=0): count+=1
    if(count>=int(k)): print('NO')
    else: print('YES')