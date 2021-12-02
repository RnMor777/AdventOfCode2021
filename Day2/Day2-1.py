f = open("Day2.txt", "r")
arr = f.readlines()
x, y = 0, 0

for i in arr:
    cmd, num = i.split(' ')
    num = int(num)
    x += num if len(cmd)==7 else 0
    y += num if len(cmd)==4 else -num if len(cmd)==2 else 0
print (x*y)
