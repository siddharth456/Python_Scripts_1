c=0
while True:
 x = input("Enter a number:")
 try:
  y=int(x)
  if y!=0:
   for i in range(y):
     for j in range(y):
        c+=1
        print(c,end=" ")
     print()
  break
 except ValueError:
    print("Invalid integer '%s'"%(x))
