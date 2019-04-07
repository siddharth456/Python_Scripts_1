# if you have a python object,you can convert it to JSON string by using json.dumps() method
import json
# a python object (dict)
x = {"name":"Amit Kumar","age":32,"city":"NY"}
# Convert to JSON
y = json.dumps(x)
# print object type
print(type(y))
# print object
print(y)