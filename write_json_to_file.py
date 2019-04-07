# Writes a JSON to a file
# json.dump() method is used to write the json string to a writeable object 
import json
data = {}
data['people']=[]
data['people'].append({"Name":"John Doe",
                       "Age":27,
                       "Website":"www.john-d.com"})
data['people'].append({"Name":"Brian Mosers",
                       "Age":34,
                       "Website":"www.automatewithbrian.org"})
data['people'].append({"Name":"Dr.Dre",
                       "Age":45,
                       "Website":"www.kingdre.au"})
print(data)
with open('json_testfile.txt','w') as f:
    json.dump(data,f,indent=4)

