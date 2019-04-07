from itertools import cycle
x=['apple','orange','bananas']
count=0
for i in cycle(x):
    if count>8:
        break
    print(i)
    count+=1


