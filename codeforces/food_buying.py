t = int(input())
out = []
for i in range(t):
    n = int(input())
    val = 0
    while(n >= 10):
        a = int(n/10)
        a = a*10
        val += a
        n = n-a
        cb = int(a/10)
        n += cb
    val += n
    # print(val)
    out.append(val)
for i in out:
    print(i)
