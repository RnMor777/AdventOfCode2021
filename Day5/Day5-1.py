f = open("Day5.txt", "r")
arr = f.readlines()
marks = [[0 for j in range(1000)] for i in range(1000)] 

for i in arr:
    start, end = i.split(' -> ')
    x1, y1 = list(map(int, start.split(',')))
    x2, y2 = list(map(int, end.split(',')))
    if (x1 == x2):
        newy1, newy2 = min(y1, y2), max(y1, y2)
        for j in range(newy2-newy1+1):
            marks[newy1+j][x1] += 1
    if (y1 == y2):
        newx1, newx2 = min(x1, x2), max(x1, x2)
        for j in range(newx2-newx1+1):
            marks[y1][newx1+j] += 1

tot = 0
for i in marks:
    for j in i:
        tot += 1 if j>1 else 0

print (tot)
