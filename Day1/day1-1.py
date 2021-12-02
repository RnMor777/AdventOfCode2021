f = open("day1.txt", "r")
arr = list(map(int, f.readlines()))
print(sum([1 if arr[i+1]>arr[i] else 0 for i in range(len(arr)-1)]))
