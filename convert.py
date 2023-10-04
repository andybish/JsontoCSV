headers = ['id64', 'name', 'coords', 'date']
filename = 'systemsWithCoordinates'

import json
import csv

file = open(filename + '.json')
j = json.load(file)
file.close()
c = open(filename + '.csv', 'w')
writer = csv.writer(c, dialect='unix', escapechar='\\', doublequote=False)

writer.writerow(headers)
count = 0
missings = {}
for row in j:
    data = []
    for h in headers:
        if h in row:
            if '{' in str(row[h]):
                data.append(json.dumps(row[h]))
            else:
                data.append(row[h])
        else:
            if h not in missings:
                missings[h]=1
            else:
                missings[h]+=1
            data.append('')
    try:
        writer.writerow(data)
    except:
        print(row)
        break
    count+=1
print(count)
print(missings)
c.close()
