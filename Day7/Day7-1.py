import statistics

f = open ("Day7.txt", "r")
arr = list(map(int, f.readline().split(',')))

med = int(statistics.median(arr))
print (sum([abs(x-med) for x in arr]))
