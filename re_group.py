# demonstrates the group() method/attribute of the match Object
import re
teststr = 'Cats are smarter than dogs'
matchObj = re.match('(.*) are (.*?) (.*)',teststr)
if matchObj:
    print(matchObj.group(0))
    print(matchObj.group(1))
    print(matchObj.group(2))
    print(matchObj.group(3))
else:
    print('match not found')