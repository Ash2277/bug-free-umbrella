t = int(input())
out = []
for i in range(t):
    m = -1
    a, b, c = map(int, input().split(' '))
    if((2*b-c) % a == 0 and (2*b-c) > 0):
        m = (2*b-c)/a
    elif((a+c) % (2*b) == 0):
        m = (a+c)/(2*b)
    elif((2*b-a) % c == 0 and (2*b-a) > 0):
        m = (2*b-a)/c

    if m == -1:
        out.append('NO')
    else:
        out.append('YES')
for i in out:
    print(i)
