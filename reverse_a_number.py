rev=0
num=int(input("Enter a number:"))
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
print("the reverse of number is {0}".format(rev))