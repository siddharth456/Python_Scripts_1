# Program demonstrates the difference of two given lists

# Method-1 Using set() A-B
#def difference(lst1,lst2):
#    final_list=list(set(lst1)-set(lst2))
#    return final_list

# Method-2 Without using set
def difference(lst1,lst2):
    final_list=[i for i in lst1 + lst2 if i not in lst2]
    return final_list

# Driver Code
lst1=[1,4,7,11,15,19,23,27,31,35,39,43,47]
lst2=[1,3,5,7,21,23,41,35,39,47,50]
print(difference(lst1,lst2))