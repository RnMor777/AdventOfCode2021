def findBasin (i, j, marked, count):
    if (i<0 or i>=sizei):
        return marked, count
    elif (j<0 or j>=sizej):
        return marked, count
    elif (arr[i][j] == 9):
        return marked, count
    elif (marked[i][j] == 1):
        return marked, count

    marked[i][j]=1
    count += 1
    marked, count = findBasin(i-1,j,marked,count)
    marked, count = findBasin(i+1,j,marked,count)
    marked, count = findBasin(i,j-1,marked,count)
    marked, count = findBasin(i,j+1,marked,count)
    return marked, count

f = open ("Day9.txt", "r")
arr = f.readlines()
arr = [list(map(int, i.strip())) for i in arr]
basins = []
sizei, sizej = len(arr), len(arr[0])

for i in range(sizei):
    for j in range(sizej):
        low = True
        if (i-1 >= 0):
            low = low if arr[i-1][j]>arr[i][j] else False
        if (i+1 < sizei):
            low = low if arr[i+1][j]>arr[i][j] else False
        if (j-1 >= 0):
            low = low if arr[i][j-1]>arr[i][j] else False
        if (j+1 < sizej):
            low = low if arr[i][j+1]>arr[i][j] else False
        if (low):
            marked, count = findBasin (i, j, [[0 for k in range(sizej)] for l in range(sizei)], 0)
            basins.append(count)
basins.sort(reverse=True)
print (basins)
print (basins[0]*basins[1]*basins[2])
