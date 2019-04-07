# Given an input string str[],generate two output strings.One of which consists of those characters which occurs
# only once in the input string. The other string consists of characters occuring multiple times in the input string
# Both the strings must be sorted

from collections import Counter
def generateStrings(inputString):
    freqDict=Counter(inputString)     # created a key-value(key-frequency) pair dictionary
    freq1=[key for (key,value) in freqDict.items() if value==1 ]
    freqmore=[key for (key,value) in freqDict.items() if value>1]
    freq1.sort()
    freqmore.sort()
    print("String with 1 occurence per character in the input:",''.join(freq1))
    print("String with multiple occurence per character in the input:",''.join(freqmore))
inputString=input("Enter a string:")
generateStrings(inputString)