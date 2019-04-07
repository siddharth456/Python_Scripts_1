#the repeat function will repeat an object again and again unless there is a times argument
#itertools.repeat(object[,times])

from itertools import repeat
for i in repeat("spam",3):
    print(i)