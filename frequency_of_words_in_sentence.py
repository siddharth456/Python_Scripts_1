# The program counts the frequency of occurence of each word in the given sentence
# Replaces all punctuations with spaces using maketrans
# OrderedDict: dict subclass that remembers the order entries were added
# (as dictionaries doesn’t retain order when created)

from collections import Counter,OrderedDict
import string
sentence='''Welcome to the world!!!! of Python..Python is an awesome language to learn.You must try to 
learn the syntax'''
translator=str.maketrans(string.punctuation,' '*len(string.punctuation))   # Replace all punctuations with a space
x=sentence.translate(translator)
sentence=x.split()
frequency=Counter(sentence)
print(OrderedDict(frequency))
print("The most common words are:",frequency.most_common(2))