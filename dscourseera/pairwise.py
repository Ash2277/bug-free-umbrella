n = input()
a = input().split(' ')
b = [int(x) for x in a]
b.sort(reverse=True)
print(b[0]*b[1])
