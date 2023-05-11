n,m,a=map(int,input().split(' '))
if n%a!=0:
    n+=(a-(n%a))
if m%a!=0:
    m+=(a-(m%a))
print(int((m*n)/(a*a)))