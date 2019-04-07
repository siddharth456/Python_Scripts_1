from itertools import zip_longest
fruits=['apple','mango','guava','orange']
colors=['Red','Yellow','Green','Orange','Violet','Black','Blue']
result=zip_longest(colors,fruits,fillvalue=None)
for each in result:
    print(each)