
condition="true"
while condition=="true":
  try:
    lower=int(input("Enter lower range:"))
    upper=int(input("Enter upper range:"))
    n=int(input("Enter the number to divide:"))
    for i in range(lower,upper+1):
        if i%n==0:
            print(i,end=" ")
    condition="false"
  except:
    print("Not an integer.Re-enter...")
    continue