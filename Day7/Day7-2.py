import statistics
import math

f = open ("Day7.txt", "r")
arr = list(map(int, f.readline().split(',')))

print (statistics.mean(arr))
men = math.floor(statistics.mean(arr))
print (sum([(abs(x-men)*(abs(x-men)+1)/2) for x in arr]))
