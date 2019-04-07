# Program demonstrates union of two or more lists

def union(lst1,lst2,lst3):
    final_list=list(set().union(lst1,lst2,lst3))
    return final_list
# Driver Code
lst1=[1,2,3]
lst2=[4,5,6,7]
lst3=[8,9,10]
print(union(lst1,lst2,lst3))