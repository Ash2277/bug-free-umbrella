n=int(input())
a=input().split(' ')
for i in range(1,n+1):
    for j in range(1,n+1):
        if(int(a[j-1])==i):
            for k in range(1,n+1):
                if(int(a[k-1])==j): print(k)