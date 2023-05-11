t = int(input())
out = []
for i in range(t):
    x, va, ls = map(int, input().split(' '))
    test = x
    while x > 0 and va != 0 and x > 10:
        x = int(x/2)+10
        va -= 1
    # print(x)
    while x > 0 and ls != 0:
        x -= 10
        ls -= 1
    # print(x)
    if x <= 0:
        # print('YES')
        out.append('YES')
    else:
        # print('NO')
        out.append('NO')
for i in out:
    print(i)
