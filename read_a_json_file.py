# Read a JSON from file
import json
filepath = 'C:\\Users\\shruti\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\t5di6az8.default-1403500341678\\downloadbar\\history.json'
with open(filepath,'r') as f:
    x = json.load(f)
    y = dict(x)
    with open('test.json','w') as test:
        for key,value in y.items():
            line = str(key)+':'+str(value)
            test.write(str(line))


