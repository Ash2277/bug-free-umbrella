t = int(input())
for k in range(t):
    g = int(input())
    tot = 0
    for i in range(1, g+1):
        s = 0
        j = 1
        while(s < g):
            s = s+j
            j += 1
        if(s == g):
            tot += 1
    print(tot)
