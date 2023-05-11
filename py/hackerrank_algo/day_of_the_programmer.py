n=int(input())
if(n>=1700 and n<1918):
    if(n%4==0): print("12.09.%s"%(str(n)))
    else: print("13.09.%s"%(str(n)))
if(n>1918):
    if((n%4==0 and n%100!=0) or n==2000 or n==2400): print("12.09.%s"%(str(n)))
    else: print("13.09.%s"%(str(n)))
if(n==1918): print("26.09.1918")