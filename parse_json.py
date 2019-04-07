# If you have a JSON string,you can parse it by using the json.loads() method
# the result will be a python dictionary
# example below is to convert from JSON to Python
import json
# Some JSON
x = '{"name":"Ankit Kumar","age":30,"city":"NY"}'
# parse x
y = json.loads(x)
# Print the object type
#print(type(y))
print(y["age"])


