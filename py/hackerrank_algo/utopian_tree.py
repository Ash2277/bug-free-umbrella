n=int(input())
a=[]
for i in range(n): a.append(int(input()))
for i in a:
    count=1
    for j in range(i):
        if(j%2==0): count*=2
        else: count+=1
    print(count)