n = int(input())
s = input()
# while(True):
#     if '01' in s:
#         s = s.replace('01', '')
#     elif '10' in s:
#         s = s.replace('10', '')
#     else:
#         break
# print(len(s))
zero_count = s.count('0')
one_count = s.count('1')
out = abs(zero_count-one_count)
print(out)
