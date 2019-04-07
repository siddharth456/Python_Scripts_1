from itertools import compress
data=['Apple','Orange','Bananas','Pineapple','Grapes','Watermelon']
selections=[True,False,True,False,True,False]
result=compress(data,selections)
for each in result:
    print(each)