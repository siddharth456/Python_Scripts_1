test = []
a = int(input("Enter first digit:"))
b = int(input("Enter second digit:"))
c = int(input("Enter third digit:"))
d = int(input("Enter fourth digit:"))
for i in a,b,c,d:
    test.append(i)
for x in range(0,4):
    for y in range(0,4):
        for z in range(0,4):
            for q in range(0,4):
              if x!=y and y!=z and z!=q and x!=z and x!=q and y!=q:
                 print(test[x],test[y],test[z],test[q])
