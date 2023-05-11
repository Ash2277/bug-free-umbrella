start,end,k=input().split(' ')
count=0
for i in range(int(start),int(end)+1):
    if(abs(i-int(str(i)[::-1]))%int(k)==0):
        count+=1
print(count)