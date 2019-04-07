from itertools import filterfalse
data=[1,2,3,4,5,6,7,8,9,1,4,3,10,11]
result=filterfalse(lambda x:x<7,data)
#makes a iterator that filters elements from iterable returning only those for which the predicate is false
for each in result:
    print(each)