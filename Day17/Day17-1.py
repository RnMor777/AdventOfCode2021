maxx = 330
minx = 288
maxy = -50
miny = -96

possible = []
for x in range(maxx+1):
    for y in range(miny, 100):
        curx, cury = 0, 0
        slopex, slopey = x, y
        while (curx<=maxx and cury>=miny):
            if (curx>=minx and cury<=maxy):
                possible.append([x, y])
                break
            curx += slopex
            cury += slopey
            slopex = slopex-1 if slopex-1>0 else 0
            slopey -= 1

maxY = 0
for i in possible:
    maxY = i[1] if i[1]>maxY else maxY
print ((maxY*(maxY+1))/2)
