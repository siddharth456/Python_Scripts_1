import itertools
x=['apple','orange','bananas']
result=itertools.permutations(x,2)
for each in result:
    print(each)