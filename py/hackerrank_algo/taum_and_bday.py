t = int(input())
for i in range(t):
    b, w = map(int, input().strip().split(" "))
    bc, wc, z = map(int, input().strip().split(" "))
    a, c = int(min(bc, wc)), int(max(bc, wc))
    if(a+z <= c):
        if(a == bc):
            tot = int((a*b)+(w*(a+z)))
        else:
            tot = int((a*w)+(b*(a+z)))
    else:
        tot = int((b*bc)+(w*wc))
    print(tot)
