t = int(input())
out = []
for i in range(t):
    n, a, b = map(int, input().split(' '))
    s = 'abcdefghijklmnopqrstuvwxyz'
    ans = s[:b]*n
    ans = ans[:n]
    out.append(ans)
for i in out:
    print(i)
