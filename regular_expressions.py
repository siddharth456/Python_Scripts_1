# illustrates the regular expressions 're' module
# asks user to enter a telephone number.Checks if the number is valid
# For a successful match: the number should begin with + sign,followed by the trunk code of 1-3 digits
#followed by a dash (-) and then finally exact 10 digit number
# match() determines if the RE matches at the beginning of the string

import re
number = input("Enter a telephone number:")
#x = re.match('^[+](?!0{3})\d{1,3}[-]\d{10}',number)     # returns a match object if successful or else 'None'
x = re.match('^[+]91([-]|\d{10})',number)
if x:
    print("Ths number {0} is a valid number".format(number))
else:
    print("The number {0} is not a valid number".format(number))

