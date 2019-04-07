# the starmap function makes an iterator that computes the function using arguments obtained from the iterable
# itertools.starmap(function,iterable)

from itertools import starmap
from operator import mul
data=[(2,3),(6,8),(5,2)]
result=starmap(mul,data)
for each in result:
    print(each,end=" ")

