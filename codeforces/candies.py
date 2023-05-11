import math
t = int(input())
out = []
for i in range(t):
    n = int(input())
    a = 3
    if(n % a == 0):
        out.append(int(n/a))
    else:
        while(n % a != 0):
            a = (a+1)*2-1
            if(n % a == 0):
                out.append(int(n/a))
for i in out:
    print(i)
    # val = 0
    # for x in range(1, n):
    #     tot = 0
    #     for k in range(n):
    #         tot += (x*pow(2, k))
    #         if tot == n:
    #             val = x
    #             break
    # print(val)

    # k = int(math.log(n-1)/math.log(2))
    # print(k)

    # x = 0
    # for k in range(2, int(math.log2(n))+2):
    #     series_sum = (2**k - 1) * (2**(k-1))
    #     if n % series_sum == 0:
    #         x = n // series_sum
    #         break
    # print(x)
