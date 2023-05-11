t = int(input())
out = []
for i in range(t):
    s = input()
    co = 0
    while(True):
        if '01' in s:
            s = s.replace('01', '')
            co += 1
        elif '10' in s:
            s = s.replace('10', '')
            co += 1
        else:
            break
# print(len(s))
    if co % 2 == 1:
        # print('DA')
        out.append('DA')
    else:
        # print('NET')
        out.append('NET')
# zero_count = s.count('0')
# one_count = s.count('1')
# out = abs(zero_count-one_count)
# print(out)
for i in out:
    print(i)
