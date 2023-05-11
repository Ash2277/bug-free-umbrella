n,k=input().split(' ')
b=input().split(' ')
c=int(input())
a=[int(x) for x in b]
a.pop(int(k))
sum2=sum(a)/2
if(int(sum2)==c): print('Bon Appetit')
else: print(c-int(sum2))