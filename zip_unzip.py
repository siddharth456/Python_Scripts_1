# Demonstrate usage of zip function
Name=['Anil','Shambhu','Pankaj','Sunil']
Marks=[81,63,51,92]
Grade=['A','B','C','A+']
mapped = zip(Name,Marks,Grade)
mapped=list(mapped)
print("The mapped list is:",mapped)
print()
# Now we unzip the zipped list
namz,markz,gradz=zip(*mapped)
print("The name list is: ",namz)
print("The marks list is: ",markz)
print("The grade list is: ",gradz)
