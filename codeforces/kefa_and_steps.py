n = int(input())
a = list(map(int, input().split(' ')))
maxval = a[0]
a1 = a[1:]
count = 1
li = []
for i in a1:
    if maxval <= i:
        count += 1
        maxval = i
        li.append(count)
        # print(maxval)
    else:
        count = 1
        maxval = i
        # print(maxval)
# if li == []:
#     count += 1
# li.append(count)
# print(li)
print(max(li))
# n = int(input())
# a = list(map(int, input().split(' ')))
# count = 1
# li = 1
# for i in range(1, n):
#     if a[i] >= a[i-1]:
#         count += 1
#         li = max(li, count)
#     else:
#         # count += 1

#         count = 1
#     # li = max(li, count)
# print(li)
