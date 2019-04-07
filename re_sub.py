# the sub() method in re module replaces match with the text of your choice
import re
teststring = 'This is a test string'
#x = re.sub('t','$',teststring)
# replace the first 2 occurences
x = re.sub('t','$',teststring,2)
print(x)