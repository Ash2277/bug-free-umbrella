t = int(input())
ou = []
for i in range(t):
    n = int(input())
    s = "987654321"
    out = ''
    if n > 45:
        # print(-1)
        ou.append(-1)
    else:
        for i in s:
            if n >= int(i):
                n = n-int(i)
                out += i
            else:
                break
        if n != 0:
            # print(out+str(n))
            a = out+str(n)
            a = a[::-1]
            ou.append(a)
        else:
            # print(out)
            ou.append(out[::-1])
for i in ou:
    print(int(i))
