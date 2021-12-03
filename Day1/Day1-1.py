# opens the file to read and scans in all the lines into arr
f = open("day1.txt", "r")
arr = list(map(int, f.readlines()))

# creates an array. Puts 1 if the next is larger than the current otherwise 0
# sums the array, which is the answer
print(sum([1 if arr[i+1]>arr[i] else 0 for i in range(len(arr)-1)]))
