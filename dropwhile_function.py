from itertools import dropwhile
data=[1,2,3,4,5,6,7,8,9,10,1,4,2]
result=dropwhile(lambda x:x<5,data)
# drops element while predicate (x<5) is true.Afterwards,returns every element
for each in result:
    print(each)