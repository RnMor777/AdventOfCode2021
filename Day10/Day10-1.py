f = open("Day10.txt", "r")
arr = f.readlines()
costs = {")":3,"]":57,"}":1197,">":25137}
leftBrackets = ["(", "[", "{", "<"]
rightBrackets = [")", "]", "}", ">"]
total = 0

for i in arr:
    queue = []
    for j in i.strip():
        if (j in leftBrackets):
            queue.append(j)
        else:
            tmp = queue[-1]
            if (leftBrackets[rightBrackets.index(j)] == tmp):
                queue.pop()
            else:
                total += costs[j]
                break
print (total)
