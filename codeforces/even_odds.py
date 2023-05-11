n, k = map(int, input().split(' '))
# odd_no = []
# even_no = []
# for i in range(1, n+1):
#     if i % 2 == 1:
#         odd_no.append(i)
#     else:
#         even_no.append(i)
#     # print(odd_no)
#     # print(even_no)
#     if len(odd_no) >= k or len(even_no) >= k:
#         break
# final_li = odd_no+even_no
# print(final_li[k-1])
median = n/2
if(k < median):
    rem = ((2*k)-1)
    print(int(rem))
else:
    rem = n-median
    if n % 2 == 1:
        rem = rem-1
    print(int(2*rem))
