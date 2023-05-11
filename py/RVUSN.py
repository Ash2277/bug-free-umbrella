n=str(input())
invalid=False
if len(n)!=10 or n[0]!='1' or n[1]!='R' or n[2]!='F': print('wrong input')
else:
        if(n[5:7]=='EC'): print('Electronics and Communication Engineering')
        if(n[5:7]=='ME'): print('Mechanical Engineering')
        if(n[5:7]=='CS'): print('Computer Science and Engineering')
        if(n[5:7]=='IS'): print('Information Science and Engineering')
        if not(n[7]=='0'): print(n[7:10])
        if(n[7]=='0' and n[8]=='0'): print(n[9:10])
        else: print(n[8:10])