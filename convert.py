#star headers = ['id64', 'bodyId', 'name', 'type', 'subType', 'parents', 'distanceToArrival', 'isMainStar', 'isScoopable', 'age', 'luminosity', 'absoluteMagnitude', 'solarMasses', 'solarRadius', 'surfaceTemperature', 'orbitalPeriod', 'semiMajorAxis', 'orbitalEccentricity', 'orbitalInclination', 'argOfPeriapsis', 'rotationalPeriod', 'rotationalPeriodTidallyLocked', 'axialTilt', 'belts', 'updateTime', 'systemId64', 'systemName']
#planet headers = ['id64', 'bodyId', 'name', 'type', 'subType', 'parents', 'distanceToArrival', 'isLandable', 'gravity', 'earthMasses', 'radius', 'surfaceTemperature', 'surfacePressure', 'volcanismType', 'atmosphereType', 'atmosphereComposition', 'solidComposition', 'terraformingState', 'orbitalPeriod', 'semiMajorAxis', 'orbitalEccentricity', 'orbitalInclination', 'argOfPeriapsis', 'rotationalPeriod', 'rotationalPeriodTidallyLocked', 'axialTilt', 'rings', 'materials', 'updateTime', 'systemId64', 'systemName']
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
nones = {}
skipped = 0
for row in j:
    skip = False
    data = []
#    if row['type'] != 'Star':
    for h in headers:
        if skip == True:
            continue
        if h in row:
            if row[h] is None:
                if h not in nones:
                    nones[h]=1
                else:
                    nones[h]+=1
                if h != 'id64':
                    data.append('')
                else:
                    skipped += 1
                    skip = True
                    continue
            elif '{' in str(row[h]) or '[' in str(row[h]):
                data.append(json.dumps(row[h]).replace('�','ñ')) #fuck fdev
            else:
                data.append(str(row[h]).replace('�','ñ')) #no really, fuck fdev
        else:
            if h not in missings:
                missings[h]=1
            else:
                missings[h]+=1
            data.append('')
    if skip == True:
        continue
    try:
        writer.writerow(data)
    except:
        print(row)
        break
    count+=1
print(count)
print(missings)
print(nones)
print(skipped)
c.close()
