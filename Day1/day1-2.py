f = open("day1.txt", "r")
arr = list(map(int, f.readlines()))
print(sum([1 if sum(arr[i+1:i+4])>sum(arr[i:i+3]) else 0 for i in range(len(arr))]))
