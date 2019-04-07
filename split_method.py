# Demonstrates split() method
'''split() method returns a list of strings after breaking the given string by the specified seperator'''
# Syntax: str.split(seperator,maxsplit)
text = 'Geeks For Geeks'
# split at space
print(text.split())
#print(text.split(None))


word = 'Text:for:Test'
# split at :
print(word.split(':'))

text1 = 'This line will be split only once'
# split only once
print(text1.split(' ',1))

example='CatSatBatRat'
# Splittin at 3
test=[]
for i in range(0,len(example),3):
    splitword=example[i:i+3]
    test.append(splitword)
print(test)

