# Python script to validate an email address
# using regular expressions
import re
def emailvalidate(id):
    p=re.compile('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z_\-\.]+)\.([a-zA-Z]{2,5})')
    matchObj=p.match(id)
    if matchObj:
        print('The email {0} is valid'.format(id))
    else:
        print('Invalid id {0}'.format(id))
id = input('Enter an email id to validate:')
emailvalidate(id)

