f = open("Day2.txt", "r")
arr = f.readlines()
aim, x, y = 0, 0, 0

for i in arr:
    cmd, num = i.split(' ')
    num = int(num)
    aim += num if len(cmd)==4 else -num if len(cmd)==2 else 0
    y += num if len(cmd)==7 else 0
    x += num*aim if len(cmd)==7 else 0
print (x*y)
