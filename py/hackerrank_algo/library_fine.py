d1=input().split(' ')
d2=input().split(' ')
if((d1==d2) or (d1[2]<d2[2]) or (d1[2]==d2[2] and d1[1]<d2[1]) or (d1[2]==d2[2] and d1[1]==d2[1] and d1[0]<d2[0])):
    print(0)
else:
    if not(d1[2]==d2[2]): print(10000)
    else:
        if(d1[1]==d2[1]): print(15*(int(d1[0])-int(d2[0])))
        elif(d1[1]!=d2[1]): print(500*(int(d1[1])-int(d2[1])))