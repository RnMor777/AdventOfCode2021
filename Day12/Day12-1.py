def calcPath (node, count):
    if ()


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

print(calcPath ("start", 0))
