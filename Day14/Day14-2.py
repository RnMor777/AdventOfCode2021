f = open("Day14.txt", "r")
arr = f.readlines()
inserts = {}
doubles = {}

for i in range(len(arr[0].strip())-1):
    if (arr[0][i:i+2] in doubles):
        doubles[arr[0][i:i+2]] += 1
    else:
        doubles[arr[0][i:i+2]] = 1

for i in arr[2:]:
    key, val = i.strip().split(' -> ')
    inserts[key] = val

for i in range(40):
    newDoubles = {}
    for j in doubles:
        added = inserts[j]
        if (j[0]+added in newDoubles):
            newDoubles[j[0]+added] += doubles[j]
        else:
            newDoubles[j[0]+added] = doubles[j]

        if (added+j[1] in newDoubles):
            newDoubles[added+j[1]] += doubles[j]
        else:
            newDoubles[added+j[1]] = doubles[j]
    doubles = newDoubles

countDict = {}
for i in doubles:
    j = list(i)[0]
    if (j not in countDict):
        countDict[j] = doubles[i]
    else:
        countDict[j] += doubles[i]
countDict[arr[0][-2]] += 1

print (max(countDict.values()) - min(countDict.values()))
