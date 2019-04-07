# You can convert the following Python objects into JSON strings
# Python Object- dict,list,tuple,string,int,float,True,False,None
# JSON equivalent- Object,array,array,string,Number,Number,true,false,null
# example to convert a Python object containing all legal data types to JSON string

import json
# a python object
x = {"Name":"Siddharth Deo",
     "Age":31,
     "Married":False,
     "Divorced":False,
     "Single":True,
     "Pets":True,
     "Cars":
     [
         {"model":"Porche Cayman","year":2021},
         {"model":"BMW M5","year":2021}

     ],
     "Health Records":None
      }
# Convert to json
# format the result using indent
# default seperators are ", " ": " (comma and a space/colon and a space)
# sort_keys parameter decides whether or not to sort the result
y = json.dumps(x,indent=4,separators=(". ","="),sort_keys=True)
# Print
print(y)