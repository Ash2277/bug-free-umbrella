s = input()
lc_count = 0
uc_count = 0
for i in s:
    if i.isupper():
        uc_count += 1
    if i.islower():
        lc_count += 1
if lc_count >= uc_count:
    print(s.lower())
if uc_count > lc_count:
    print(s.upper())
