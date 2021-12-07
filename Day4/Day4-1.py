def runBingo ():
    for i in numbs:
        for j in range (len(boards)):
            for k in range(5):
                for l in range(5):
                    if (boards[j][k][l] == i):
                        marks[j][k][l] = 1
                        if (checkBoard(j) == True):
                            return j, i

def checkBoard (a):
    if (sum (marks[a][0]) == 5):
        return True
    for i in range (5):
        if (sum ([x[i] for x in marks[a]]) == 5):
            return True
    return False


f = open ("Day4.txt", "r")
arr = f.readlines()
arr = [x for x in arr if x!="\n"]
numbs = list(map(int, arr.pop(0).split(',')))
boards = []

i = 0
while (i < len (arr)):
    boards.append([list(map(int, list([x for x in arr[j].split(' ') if x != '']))) for j in range(i, i+5)])
    i += 5

marks = [[[0 for i in range (5)] for j in range(5)] for k in range(len(boards))]
winningBoard, lastNumb = runBingo()
score = 0
for i in range (5):
    for j in range(5):
        if (marks[winningBoard][i][j] == 0):
            score += boards[winningBoard][i][j]
print (score*lastNumb)
