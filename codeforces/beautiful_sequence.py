# def printSubsequences(arr, index, subarr):
#     li = []
#     countt = 0
#     if index == len(arr):
#         if len(subarr) != 0:
#             # print(subarr)
#             for i in range(len(subarr)):
#                 if subarr[i] == i+1:
#                     countt += 1
#             # print(countt)
#             if countt > 0:
#                 # print('YES')
#                 return 'YES'

#             # li.append(subarr)

#     else:
#         printSubsequences(arr, index + 1, subarr)
#         printSubsequences(arr, index + 1,
#                           subarr+[arr[index]])
#     # print(li)
#     return


def subsequences(ind, ans, l, n):
    final_ans = []
    if ind == n:
        return [ans]
    else:
        final_ans.extend(subsequences(ind+1, ans + [l[ind]], l, n))
        final_ans.extend(subsequences(ind+1, ans, l, n))
        return final_ans


t = int(input())
out = []
for i in range(t):
    n = int(input())
    seq = list(map(int, input().split(' ')))
    subseq = []
    ans = subsequences(0, [], seq, n)

    for i in ans:
        countt = 0
        for j in range(len(i)):
            if i[j] == j+1:
                countt += 1
                out.append('YES')
                break
        # print(countt)
        if countt > 0:
            # out.append('YES')
            break
        if i == ans[-1] and countt == 0:
            out.append('NO')
# print(out)
for i in out:
    print(i)
# print(ans)
