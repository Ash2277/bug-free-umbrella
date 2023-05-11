t = int(input())
for k in range(t):
    l = int(input())
    s = input()
    i = 1
    a = []
    b = 0
    while(i < l):
        if(s[i-1] < s[i]):
            a.append(s[b:i])
            i += 1
        else:
            a.append(s[b:i])
            b = i
            i += 1
    if(s[l-1] < s[l-2]):
        a.append(s[l-1])
    else:
        a.append(s[b:l])
    print("Case #"+str(k+1)+": ", end="")
    for j in a:
        print(len(j), end=" ")
