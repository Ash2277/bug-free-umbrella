s=input()
s=s.lower()
l=list(s)
vow=['a','e','i','o','u','y']
l2=[]
for i in l:
    if i not in vow:
        l2.append("."+i)
s2=""
for i in l2:
    s2+=i
print(s2)    