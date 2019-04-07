# demonstrates the findall() method in re module
# findall() method returns a list containing all matches
# find all substrings where the RE matches, and returns them as a list.

import re
str = 'The train in Spain'
x = re.findall('ai',str)
# returns an empty list in case of no match
#x = re.findall('Portugal',str)
print(x)