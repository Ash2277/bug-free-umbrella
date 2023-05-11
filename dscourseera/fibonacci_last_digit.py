# Uses python3
n = int(input())
# a = [0, 1]
# if(n == 0):
#     print('0')
# elif(n == 1):
#     print('1')
# else:
#     for i in range(2, n+1):
#         b = a[i-1]+a[i-2]
#         a.append(b)
#     c = str(a[-1])
#     print(c[-1])


def last_digit(n):
    a, b = 0, 1
    for i in range((n + 2) % 60):
        a, b = b, (a + b) % 10
    return 9 if a == 0 else a - 1


print(last_digit(n))
