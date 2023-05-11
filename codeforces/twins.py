n = int(input())
coins = list(map(int, input().split(' ')))
coins.sort(reverse=True)
# print(coins)
for i in range(n+1):
    value1 = sum(coins[:i])
    value2 = sum(coins[i:])
    # print(value1)
    # print(value2)
    if(value1 > value2):
        print(len(coins[:i]))
        exit()
