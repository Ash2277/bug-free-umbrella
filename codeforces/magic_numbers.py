n = input()
if '144' in n:
    n = n.replace('144', '*')
if '14' in n:
    n = n.replace('14', '*')
if '1' in n:
    n = n.replace('1', '*')
if '*' in n:
    n = n.replace('*', '')
if n == '':
    print('YES')
else:
    print('NO')
