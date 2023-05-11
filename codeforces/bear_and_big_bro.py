limak_weight, bob_weight = map(int, input().split(' '))
count = 0
while limak_weight <= bob_weight:
    limak_weight *= 3
    bob_weight *= 2
    count += 1
print(count)
