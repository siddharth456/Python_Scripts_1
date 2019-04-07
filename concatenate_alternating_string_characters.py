condition='true'
while condition=='true':
   temp=[]
   a=input("Enter a string:")
   b=input("Enter another string:")
   x,y=len(a),len(b)
   joined_string=list(a)+list(b)
   if x==y:
      for i in range(x):
        if i==0:
            n=joined_string[::x]
            continue
        nx=joined_string[i::x]
        temp=temp+nx            #We use a temporary list to store result with every iteration
      final=n+temp
      print("the desired concatenated string is:",''.join(final))
      condition='false'
   else:
      print("the two strings are of unequal length")
      continue




