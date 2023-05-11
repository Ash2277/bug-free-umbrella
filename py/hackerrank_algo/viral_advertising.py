n=int(input())
a,c=5,0
for i in range(n):
    b=int(a/2)
    c=c+b
    a=b*3
print(c)