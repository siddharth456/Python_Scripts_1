import itertools
data=[5,2,6,4,5,9]
result=itertools.accumulate(data)
for i in result:
    print(i)