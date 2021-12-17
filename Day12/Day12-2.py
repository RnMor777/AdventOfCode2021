def calcPath (node, count, hops, smallCave):
    if (node == "end"):
        print (hops)
        return count+1

    for i in paths[node]:
        if (i=="start"):
            continue
        if (i.islower() and i in hops.split(',') and smallCave==True):
            continue
        if (i.islower() and i in hops.split(',')):
            count = calcPath (i, count, hops+i+",", True)
        else:
            count = calcPath (i, count, hops+i+",", smallCave)
    return count

f = open("Day12.txt", "r")
arr = f.readlines()
paths = {}
count = 0

for i in arr:
    start, end = i.strip().split('-')
    if (start in paths):
        paths[start].append(end)
    else:
        paths[start] = [end]

    if (end in paths):
        paths[end].append(start)
    else:
        paths[end] = [start]

print(calcPath ("start", 0, "", False))
