# both the strings must be of equal length
from itertools import zip_longest
v1=list('abcx')
v2=list('defy')
result=zip_longest(v1,v2)
for each in result:
    print(''.join(each),sep="",end="")
