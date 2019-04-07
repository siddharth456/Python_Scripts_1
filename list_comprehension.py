#Creates a list containing 5 lists, each of 8 items, all set to 0
#w, h = 8, 5
#Matrix = [[0 for x in range(w)] for y in range(h)]
#print(Matrix)

# pd = [[1,2,3] for x in range(3)]
# print(pd)

combo=[(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y ]
print(combo)

# flatten a list of lists
lol=[[1,2,3],[4,5,6],[7,8,9]]
flat=[num for elem in lol for num in elem]
print(flat)

# Now we transpose the 3X3 matrix lol
transpose=[[elem[i] for elem in lol] for i in range(3)]
print(transpose)

# Use zip function to transpose a matrix even faster
print(list(zip(*lol)))