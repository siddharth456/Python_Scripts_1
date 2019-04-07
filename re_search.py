# demonstrates the search() method in re module
# the search() method scans through a string for a match and returns a match object if there is a match
# if there is more than one match,only the first occurence is returned
import re
str = 'This is a test line with few whitespaces'
x = re.search('\s',str)
print("The first whitespace character in the string is at position:",x.start())