# islice() function is very similar to slices. It allows you to cut out a piece of an iterable
# itertools.islice(iterable,start,stop[, step])
from itertools import islice

colors=['red','blue','green','orange','blue']
few_colors=islice(colors,2)
for each in few_colors:
    print(each)
