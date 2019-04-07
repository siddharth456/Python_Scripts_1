import operator
import itertools
data=[1,2,3,4,5]
result=itertools.accumulate(data,operator.mul)
for each in result:
    print(each)