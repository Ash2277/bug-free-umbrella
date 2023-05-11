n=input()
def last(s):
    return s[-1]
a=n.split(' ')
a.sort(key=last)
b=[x[:-1] for x in a]
for i in b: print(i,end=' ')