''' List out all possible combinations of 3 digits'''

testlist=[]
a=int(input("Enter first digit:"))
b=int(input("Enter second digit:"))
c=int(input("Enter third digit:"))
for i in a,b,c:
    testlist.append(i)
for x in range(0,3):
    for y in range(0,3):
        for z in range(0,3):
            if x!=y and y!=z and x!=z:
                print(testlist[x],testlist[y],testlist[z])