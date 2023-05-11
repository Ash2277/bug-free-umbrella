f,g,c,d,e=input().split(' '),input().split(' '),input().split(' '),input().split(' '),input().split(' ')
s,t,a,b,m,n,c1,c2=int(f[0]),int(f[1]),int(g[0]),int(g[1]),int(c[0]),int(c[1]),0,0
x=[a+int(d[i]) for i in range(len(d))]
y=[b+int(e[i]) for i in range(len(e))]
for i in x: 
    if(i>=s and i<=t): c1+=1
for i in y:
    if(i>=s and i<=t): c2+=1
print(c1)
print(c2)