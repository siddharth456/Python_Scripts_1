'''read a number n and print and compute the series “1+2+3+…+n=" '''
c=0
x=int(input("Enter a number:"))
for i in range(1,x+1):
    print(i,sep=" ",end="")
    if i<x:
        print("+",sep=" ",end="")
    c+=i
print("={0}".format(c))