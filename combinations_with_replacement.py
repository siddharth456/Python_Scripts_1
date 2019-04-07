import itertools
x=['apple','orange','bananas']
result=itertools.combinations_with_replacement(x,2)
for each in result:
    print(each)