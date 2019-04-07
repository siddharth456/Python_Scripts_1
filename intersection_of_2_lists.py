# Program to illustrate the intersection of two lists

# Method-1
#def intersection(lst1,lst2):
#    lst3=[i for i in lst1 if i in lst2]
#    return lst3

# Method-2
#def intersection(lst1,lst2):
#    lst3=list(set(lst1) & set(lst2))
#    return lst3

# Method-3
def intersection(lst1,lst2):
    lst3=set(lst1).intersection(lst2)
    return lst3

#Driver Code
lst1=[1,4,7,11,15,19,23,27,31,35,39,43,47]
lst2=[1,3,5,7,21,23,41,35,39,47,50]
print(intersection(lst1,lst2))

