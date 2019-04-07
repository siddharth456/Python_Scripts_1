from itertools import chain
x=['apple','orange','bananas']
y=['Red','Orange','Yellow']
result=chain(x,y)
for each in result:
    print(each)