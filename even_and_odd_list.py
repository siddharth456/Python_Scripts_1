# Program to split a list of numbers into two seperate lists of even and odd numbers
testlist=[1,3,17,2,54,100,98,24,87,88,90,46]
evenlist=[]
oddlist=[]
for i in testlist:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print(evenlist)
print(oddlist)