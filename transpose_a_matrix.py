lol=[[1,2,3],[4,5,6],[7,8,9]]
transposed = []
for i in range(3):
    transposed_row= []
    for elem in lol:
        transposed_row.append(elem[i])
    transposed.append(transposed_row)
print(transposed)
