n=int(input())
a=input().split(' ')
i=0
b=0
while(i<=len(a)):
    
    if((a[i-1]=='0' and a[i-2]=='0') or (a[i-1]!='0' and a[i-2]=='0')):
        i=i+2
        b=b+1
    elif(a[i-1]=='0' and a[i-2]!='0'):
        i=i+1
        b=b+1
print(b-1)