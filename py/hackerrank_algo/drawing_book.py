# SIMPLE METHOD(got it online)
# n = int(input().strip())
# p = int(input().strip())
# print(min(p//2, (n-p)//2))
# DUMB METHOD(which i came up with)
n,p=int(input()),int(input())
temp,temp1,a,page1=0,0,2,1
if(p==1): print(0)
elif(p==n and n%2==0): print(0)
elif(n%2!=0 and (p==n or p==n-1)): print(0)
else:
    while(a<=n):
        for j in range(1,3):
            if(a==p):
                temp=1
                break
            else: a=a+1
        if not(temp==1): page1=page1+1
        else: break
    if(n%2==0): page2,b=1,n-1
    else: page2,b=0,n
    while(b>0):
        for j in range(1,3):
            if(b==p):
                temp1=1
                break
            else: b=b-1
        if not(temp1==1): page2=page2+1
        else: break
    if(page2>page1): print(page1)
    elif(page1>page2): print(page2)
    else: print(page2)