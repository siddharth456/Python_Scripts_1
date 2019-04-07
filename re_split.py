# the split() method returns a list where the string has been split at each match
import re
str = 'This is a test string'
x = re.split('\s',str,2)   # maxsplit=2
print(x)