# opens the file to read and scans in all the lines into arr
f = open("day1.txt", "r")
arr = list(map(int, f.readlines()))


# creates an array. Puts 1 if the next block of 3 is larger than the current otherwise 0
# sums the array, which is the answer
print(sum([1 if sum(arr[i+1:i+4])>sum(arr[i:i+3]) else 0 for i in range(len(arr))]))
