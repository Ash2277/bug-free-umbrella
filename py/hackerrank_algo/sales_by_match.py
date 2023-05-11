n=input()
b=input().split(' ')
a=[int(x) for x in b]
a.sort()
pair,i=0,1
while(i<len(a)):
    if(a[i-1]==a[i]):
        pair=pair+1
        i=i+2
    else: i=i+1
print(pair)
