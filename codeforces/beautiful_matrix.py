for i in range(5):
    row = list(map(int, input().split(' ')))
    if 1 in row:
        column_no = row.index(1)+1
        row_no = i+1
moves = 0
while row_no != 3 or column_no != 3:
    if row_no < 3:
        row_no += 1
        moves += 1
    if row_no > 3:
        row_no -= 1
        moves += 1
    if column_no < 3:
        column_no += 1
        moves += 1
    if column_no > 3:
        column_no -= 1
        moves += 1
print(moves)
# print(column_no)
