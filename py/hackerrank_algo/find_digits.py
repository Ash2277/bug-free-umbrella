t=int(input())
for i in range(t):
    n=str(input())
    a,c=list(n),0
    for i in a:
        if not(i=='0'):
            if(int(n)%int(i)==0): c+=1
    print(c)