def dikstra (node):
    dist = [9999999 for x in range(nodeAmt)]
    mark = [False for x in range(nodeAmt)]
    
    dist[node] = 0;
    while (1):
        v = 0
        for i in range(nodeAmt-1, -1, -1):
            if (mark[i] == False and dist[i] <= dist[v]):
                v = i

        if (v == 0):
            break

        mark[v] = True
        for i in range(0, nodeAmt):
            if (matrix[i][v] and mark[i]==False):
                if (dist[v]+matrix[i][v] < dist[i]):
                    dist[i] = dist[v] + matrix[i][v]
    return dist

f = open("Day15.txt", "r")
arr = [list(map(int, list(x.strip()))) for x in f.readlines()]
xlen = len(arr[0])
ylen = len(arr)
nodeAmt = xlen*ylen
matrix = [[0 for i in range(nodeAmt)] for j in range(nodeAmt)]

for y in range(ylen):
    for x in range(xlen):
        if (y-1>=0):
            matrix[x+y*xlen][x+(y-1)*xlen] = arr[y-1][x]
        if (y+1<ylen):
            matrix[x+y*xlen][x+(y+1)*xlen] = arr[y+1][x]
        if (x-1>=0):
            matrix[x+y*xlen][(x-1)+y*xlen] = arr[y][x-1]
        if (x+1<xlen):
            matrix[x+y*xlen][(x+1)+y*xlen] = arr[y][x+1]

print (dikstra(nodeAmt-1)[0])
