''' read a number n and print the natural numbers summation pattern
For example
Case 1:
Enter a number: 4
1 = 1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10

Case 2:
Enter a number: 5
1 = 1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
1 + 2 + 3 + 4 + 5 = 15'''

c=0
x=int(input("Enter a number:"))
for j in range(1,x+1):
    for i in range(1,j+1):
       print(i,sep=" ",end=" ")
       if i<j:
         print("+",sep=" ",end=" ")
    c+=i
    print("=",c)






