'''Prints an inverted star pattern
For example

Enter a number:5

*****
 ****
  ***
   **
    *  '''

x=int(input("Enter a number:"))
for i in range(x,0,-1):
    print((x-i)*' '+i*'*')