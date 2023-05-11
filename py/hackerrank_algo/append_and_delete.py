#failed 1 case
n1=input()
n2=input()
n3=""
n4=""
k=int(input())
if(n1==n2):
    print('Yes')
else:
    i=0
    while(i<len(n1) and i<len(n2)):
        if(n1[i]==n2[i]):
            n3+=n1[i]
            i+=1
        else:
            break
    if not n3==n1:
        count=len(n1)-len(n3)
        n4+=n2[len(n3):]
        count=count+len(n4)
        if(count<=k):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
#online
# s = input().strip()
# t = input().strip()
# k = int(input().strip())

# i = 0
# while i < len(t) and i < len(s):
#     if s[i] != t[i]:
#         break
#     i += 1

# if i < len(s):
#     k -= len(s[i:])
# if i < len(t):
#     k -= len(t[i:])
# if k >= 0 and (k % 2 == 0 or k - 2 * i >= 0):
#     print("Yes")
# else:
#     print("No")