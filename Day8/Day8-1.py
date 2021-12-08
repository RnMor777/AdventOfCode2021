f = open("Day8.txt", "r")
arr = f.readlines()

tot = 0
for i in arr:
    x, y = i.split(' | ')
    yarr = list(y.strip().split(' '))
    out = [j for j in yarr if len(j)==2 or len(j)==3 or len(j)==4 or len(j)==7]
    tot += len(out)

print (tot)
