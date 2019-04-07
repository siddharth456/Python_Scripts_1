# Generate all possible permutations of a set

# Method-1 Using itertools
#from itertools import permutations
#x=list(permutations(range(1,4)))    # Set is (1,2,3)
#print(x)

# Method-2 Backtracking based recursive solution
def permutations(testlist):
    if len(testlist)==0:    # if the list is empty then there are no possible permutations
        return []
    if len(testlist)==1:  # if the list has only 1 element then return that element
        return testlist
    l=[]
    for i in range(len(testlist)):
        m = testlist[i]
        remlist = testlist[:i] + testlist[i+1:]
        for p in permutations(remlist):
            l.append([m]+list(p))
    return l
#Driver Code
testlist=list('123')
print(permutations(testlist))


