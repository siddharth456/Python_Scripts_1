# itertools.groupby(iterable,key[optional])
# groupby function takes two arguments: an iterable(list,tuple,dictionary) and a key function which calculates keys for
# each element present in iterable.

from itertools import groupby
data=(1,1,1,3,3,2,2,2,2,5,5,5,5)
for (key,group) in groupby(data):
    print(key,list(group))