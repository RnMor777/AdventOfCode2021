f = open("Day6.txt", "r")
arr = list(map(int, f.readline().split(',')))
numbs = []
for i in range(9):
    numbs.append(len([x for x in arr if x==i]))

for i in range (256):
    tmp = numbs.pop(0)
    numbs.append(tmp)
    numbs[6] += tmp

print (sum(numbs))
