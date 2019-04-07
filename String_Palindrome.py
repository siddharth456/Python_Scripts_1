x=input("Enter a string:")
str=''
for i in x:
    str=i+str
if x==str:
    print("{0} is a palindrome string".format(x))
else:
    print("{0} is not a palindrome string".format(x))
