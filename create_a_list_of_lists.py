
x=int(input("Enter no of items in the list:"))
pd= [[] for i in range(x)]
for a in pd:
    for b in range(3):
       y=input("Enter element in list index "+str(a))
       a.append(y)
print(pd)
