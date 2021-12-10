f = open ("Day9.txt", "r")
arr = f.readlines()
arr = [list(map(int, i.strip())) for i in arr]
tot = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        low = True
        if (i-1 >= 0):
            low = low if arr[i-1][j]>arr[i][j] else False
        if (i+1 < len(arr)):
            low = low if arr[i+1][j]>arr[i][j] else False
        if (j-1 >= 0):
            low = low if arr[i][j-1]>arr[i][j] else False
        if (j+1 < len(arr[i])):
            low = low if arr[i][j+1]>arr[i][j] else False
        if (low):
            tot += arr[i][j]+1
print (tot)
