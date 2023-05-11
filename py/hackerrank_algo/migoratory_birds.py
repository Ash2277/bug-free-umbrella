#online
#n = int(input())
#array = (input().split(' '))
#ml = [0]*n
#for i in array:
#    ml[int(i)] += 1
#print(ml.index(max(ml)))
#my code
n=input()
a=input().split(' ')
count1,id1=1,0
for i in range(len(a)):
    count=0
    count = a.count(a[i])
    if(count>count1): count1,id1=count,a[i]
    elif(count1==count and int(i)<int(id1)): id1=a[i]
print(id1)