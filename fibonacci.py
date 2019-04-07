# Generates the fibonacci series
# 0 1 1 2 3 5 8 13...
#a,b=0,1
#while a<100:
#   print(a,end=" ")
#   a,b=b,a+b
'''We implement the same by defining a function and calling it'''
def fib(n):
   result=[]
   a,b=0,1
   while a<n:
      result.append(a)
      a,b=b,a+b
   return result
n=int(input("Enter a number:"))
print(fib(n))       # prints the return value of the called function

