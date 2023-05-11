from math import sqrt
t = int(input())
out = []
# for i in range(t):
#     n = int(input())
#     if n % 2 == 1:
#         out.append('YES')
#     else:
#         val = 3
#         flag = False
#         # while(n > 0):
#         while(val <= int(sqrt(n))+1):
#             if n % val == 0:
#                 flag = True
#                 break
#             else:
#                 val += 2
#         if flag == True:
#             out.append('YES')
#         else:
#             out.append('NO')
# for i in out:
#     print(i)

for i in range(t):
    n = int(input())
    flag = False
    if n % 2 == 1:
        out.append('YES')
    else:
        while(n > 2):
            rem = n % 2
            n = n/2
            if rem == 1:
                flag = True
                break
        if flag == True:
            out.append('YES')
        else:
            out.append('NO')
for i in out:
    print(i)
