import math

f = open("Day10.txt", "r")
arr = f.readlines()
costs = {")":3,"]":57,"}":1197,">":25137}
leftBrackets = ["(", "[", "{", "<"]
rightBrackets = [")", "]", "}", ">"]
sums = []

for i in arr:
    queue = []
    illegal = False
    for j in i.strip():
        if (j in leftBrackets):
            queue.append(j)
        else:
            tmp = queue[-1]
            if (leftBrackets[rightBrackets.index(j)] == tmp):
                queue.pop()
            else:
                illegal = True
                break
    if (not illegal):
        total = 0
        while (len(queue) != 0):
            total *= 5
            total += (1+leftBrackets.index(queue.pop()))
        sums.append(total)
            
sums.sort()
print (sums[math.floor(len(sums)/2)])
