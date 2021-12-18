f = open("Day14.txt", "r")
arr = f.readlines()
init = arr[0].strip()
inserts = {}

for i in arr[2:]:
    key, val = i.strip().split(' -> ')
    inserts[key] = val

for i in range(10):
    newInit = ''
    for j in range(len(init)-1):
        newKey = inserts[init[j:j+2]]
        newInit += init[j] + newKey
    newInit += init[-1]
    init = newInit

countDict = {}
for i in init:
    if (i not in countDict):
        countDict[i] = 1
    else:
        countDict[i] += 1

print (max(countDict.values()) - min(countDict.values()))
