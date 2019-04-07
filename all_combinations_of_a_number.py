import itertools
x=int(input("Enter a number:"))
a=list(str(x))
# using set will eliminate duplicates
# using list will include duplicates
combinations=set(itertools.permutations(a,len(a)))
for i in combinations:
    temp=''.join(i)
    print(temp)
