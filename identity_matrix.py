'''Prints an identity matrix'''

x=int(input("Enter a number:"))
for i in range(0,x):
    for j in range(0,x):
        if i==j:
          print("1",sep=" ",end=" ")
        else:
          print("0",sep=" ",end=" ")
    print()
