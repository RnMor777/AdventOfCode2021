def flashRecursive (i, j):
    if (i<0 or i>9 or j<0 or j>9):
        return

    global count
    
    arr[i][j] += 1
    if (arr[i][j] > 9 and flash[i][j] == 0):
        flash[i][j] = 1
        count += 1
        for m in range(-1,2):
            for n in range(-1,2):
                if (m==0 and n==0):
                    continue
                flashRecursive(m+i, n+j)


f = open("Day11.txt", "r")
arr = [list(map(int, list(x.strip()))) for x in f.readlines()]
flash = [[0 for i in range(10)] for j in range(10)]
count = 0

for i in range (100):
    flash = [[0 for i in range(10)] for j in range(10)]
    for j in range(10):
        for k in range(10):
            arr[j][k] += 1
            if (arr[j][k] > 9):
                flashRecursive(j, k)
    for j in range(10):
        for k in range(10):
            if (arr[j][k] > 9):
                arr[j][k] = 0

print (count)
