n=float(input())
a=str(input()).split(' ')
b=[int(i) for i in a if int(i)>0]
c=[int(i) for i in a if int(i)<0]
d=[int(i) for i in a if int(i)==0] 
print(' %.6f\n'%float(len(b)/n),'%.6f\n'%float(len(c)/n),'%.6f'%float(len(d)/n))