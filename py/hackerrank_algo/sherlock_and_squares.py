#my code too long freakin again
import math 
t=int(input())
for i in range(t):
    count=0
    a=input().split(' ')
    for i in range(int(a[0]),int(a[1])+1):
        if(i%math.sqrt(i)==0.0):
            count+=1
    print(count)
#online
# import math 
# t=int(input())
# for i in range(t):
#     a=input().split(' ')
#     print((math.floor(math.sqrt(int(a[1]))) - math.ceil(math.sqrt(int(a[0]))) + 1))