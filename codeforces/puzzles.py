# n, m = map(int, input().split(' '))
# li = list(map(int, input().split(' ')))
# li.sort()
# a = li[:n]
# # print(a)
# print(max(a)-min(a))

# n, m = map(int, input().split(' '))
# li = list(map(int, input().split(' ')))
# a = []
# li.sort()
# print(li)
# for i in range(0, len(li)-n+1):
#     a.append(li[i:n+i])
# print(a)
# val = 1000000000
# for i in a:
#     if(max(i)-min(i) < val):
#         val = max(i)-min(i)
#         # print(val)
# print(val)

n, m = map(int, input().split(' '))
li = list(map(int, input().split(' ')))
a = []
val = 1000000000
li.sort()
# print(li)
for i in range(0, len(li)-n+1):
    if(max(li[i:n+i])-min(li[i:n+i]) < val):
        val = max(li[i:n+i])-min(li[i:n+i])
    # a.append(li[i:n+i])
    # if()
# print(a)

# for i in a:
    # if(max(i)-min(i) < val):
        # val = max(i)-min(i)
        # print(val)
print(val)
