n = input()
zero_count = 0
one_count = 0
for i in n:
    if i == '0':
        zero_count += 1
        one_count = 0
    if i == '1':
        one_count += 1
        zero_count = 0
    if zero_count > 6 or one_count > 6:
        print('YES')
        exit()
print('NO')
