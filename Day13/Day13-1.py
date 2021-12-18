f = open("Day13.txt", "r")
arr = f.readlines()
dots = arr[:861]
folds = arr[862:]
x, y = 1311, 895
grid = [[0 for i in range(x)] for j in range(y)]

for i in dots:
    j, k = list(map(int, i.split(',')))
    grid[k][j] = 1

for i in folds:
    val = int(i[13:])
    if (i[11] == 'x'):
        grid2 = [[grid[k][j] for j in range(x-1, val, -1)] for k in range(y)]
        grid = [[1 if grid[k][j]==1 or grid2[k][j]==1 else 0 for j in range(val)] for k in range(y)]
        x = val
    else:
        print ("yeet")

    break
print (sum([sum(x) for x in grid]))
