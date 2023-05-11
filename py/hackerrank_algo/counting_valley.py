n=int(input())
a=list(input())
seal,steps,valley=-1,0,0
for i in a:
    if(i=='U'): steps=steps+1
    elif(i=='D'): steps=steps-1
    if(steps==seal and i!='U'): valley=valley+1
print(valley)
