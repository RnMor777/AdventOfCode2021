f = open("Day6.txt", "r")
arr = list(map(int, f.readline().split(',')))

for i in range(80):
    x = len(arr)
    for j in range(x):
        arr[j] -= 1
        if (arr[j] == -1):
            arr[j] = 6
            arr.append(8)
print (len(arr))
