t = int(input())
out = []
for i in range(t):
    #     n = int(input())
    #     # s=int(n)
    #     while(n > 0):
    #         if(n % 2021 == 0 or n % 2021 == 2020 or n % 2021 == 2018):
    #             n = n-2021
    #         elif(n % 2020 == 0):
    #             n = n-2020
    #         else:
    #             out.append('NO')
    #             break
    #     if n <= 0:
    #         out.append('YES')
    # for i in out:
    #     print(i)

    #     n = input()
    #     s = int(n)
    #     while(s > 0):
    #         if(int(n[-1]) > 0):
    #             s = s-2021
    #             n = str(s)
    #         if(int(n[-1]) == 0 and len(n) > 1):
    #             s = s-2020
    #             n = str(s)
    #     # print(s)
    #     if(s < 0):
    #         out.append('NO')
    #         # print('NO')
    #     if(s == 0):
    #         out.append('YES')
    #         # print('YES')
    # for i in out:
    #     print(i)
    n = int(input())
    val = n % 2021
    if val > 0:
        a = 2021-val
        n = n-(a*2020)
    while(n > 0):
        n -= 2021
    if n == 0:
        # print('YES')
        out.append('YES')
    else:
        # print('NO')
        out.append('NO')
for i in out:
    print(i)
