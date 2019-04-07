import itertools
data=[5,2,6,4,5,9,1]
result=itertools.accumulate(data,max)
for each in result:
    print(each)