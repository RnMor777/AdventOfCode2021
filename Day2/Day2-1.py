# Opens file and writes data to arr
f = open("Day2.txt", "r")
arr = f.readlines()

# variables for x and y positions
x, y = 0, 0

# loops through by splitting input and then doing proper command
for i in arr:
    cmd, num = i.split(' ')
    num = int(num)
    x += num if len(cmd)==7 else 0
    y += num if len(cmd)==4 else -num if len(cmd)==2 else 0
print (x*y)
