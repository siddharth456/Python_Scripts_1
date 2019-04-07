# Eliminate consecutive duplicates in a string using groupby method
# Example: Input:aaaaabbbbb Output:ab
# Example: Input:GeeksForGeeks Output:GeksForGeks

from itertools import groupby
def removeallconsecutive(x):
    result=[]
    for (key,group) in groupby(x):
        result.append(key)
    print(''.join(result))
condition='true'
while condition=='true':
    x=input("Enter a string:")
    if x=='exit':
        condition='false'
        continue
    removeallconsecutive(x)
    continue


