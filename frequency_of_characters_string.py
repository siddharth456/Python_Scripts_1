# Program that finds the number of occurence(s) of characters in a string

from collections import Counter
def frequency(inputString):
    freq=Counter(inputString)
    for (key,value) in sorted(freq.items(),reverse=True):    # This is how we sort a dictionary
        print('Key:%s Value:%s'%(key,value))
inputString=input("Enter a string:")
frequency(inputString)


