n=input()
s=input().split(' ')
a=[int(x) for x in s]
min1,max1=a[0],a[0]
count1,count2=0,0
for i in a:
    if(i<min1):
        min1=i
        count1=count1+1
for i in a:
    if(i>max1):
        max1=i
        count2=count2+1
print(count2,count1)