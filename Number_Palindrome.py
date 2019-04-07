rev=0
x=int(input("Enter a number:"))
temp=x
while x>0:
    dig=x%10
    rev=rev*10+dig
    x=x//10
if temp==rev:
    print("The number {0} is a palindrome".format(temp))
else:
    print("The number {0} is not a palindrome".format(temp))