n,k=input().split(' ')
a=input().split(' ')
b,energy=int(k),100
while b<=int(n):
    if(b<int(n)and b!=int(n)):
        if(b>int(n)-int(k)):
            if(a[b]=='1'): energy-=3
            elif(a[b]=='0'): energy-=1
            b=int(k)-(int(n)-b)
        else:
            if(a[b]=='1'): energy-=3
            elif(a[b]=='0'): energy-=1
            b=b+int(k)
    elif(b==int(n)):
        if(a[0]=='1'): energy-=3
        elif(a[0]=='0'): energy-=1 
        break
print(energy)