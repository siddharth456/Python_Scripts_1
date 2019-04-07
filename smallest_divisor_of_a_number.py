x=int(input("Enter a number:"))
test=[]
for i in range(2,x+1):
    if x%i==0:
        test.append(i)
test.sort()
print("the smallest divisor of the number {0} is {1}".format(x,test[0]))