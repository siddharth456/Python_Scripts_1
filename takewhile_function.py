# the takewhile() function is kind of opposite of the dropwhile() function.It makes an iterator and returns elements
# from the iterable as long as the predicate is true

from itertools import takewhile
data=[1,2,3,4,5,6,7,8,9,10,4,2,7,9]
result=takewhile(lambda x:x<7,data)
for each in result:
    print(each)
