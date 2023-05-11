t = int(input())
out = []
for i in range(t):
    n, a, b, c, d = map(int, input().split())
    g1 = a-b
    g2 = a+b
    s1 = c-d
    s2 = c+d
    val1 = g1*n
    val2 = g2*n
    if val1 > s2:
        # print('NO')
        out.append('No')
    elif val2 < s1:
        # print('NO')
        out.append('No')
    elif val1 == s1 or val1 <= s2 or val2 >= s1 or val2 == s2:
        # print('YES')
        out.append('Yes')
for i in out:
    print(i)
