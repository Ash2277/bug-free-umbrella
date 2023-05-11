t = int(input())
out = []
for i in range(t):
    n = int(input())
    moves = 0
    if n == 1:
        moves = 0
    while(n != 1):
        if n % 6 == 0:
            n = n/6
            moves += 1
        elif (n % 6) % 2 == 0:
            moves = -1
            break
        elif (n % 6) % 2 == 1:
            n = n*2
            moves += 1
    out.append(moves)
for i in out:
    print(i)
