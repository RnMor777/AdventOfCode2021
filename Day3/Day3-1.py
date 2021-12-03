f = open("Day3.txt", "r")
arr = f.readlines()
out = ""

for i in range(len(arr[0])-1):
    c0, c1 = 0, 0
    for j in range(len(arr)):
        if (arr[j][i] == '0'):
            c0 += 1
        elif (arr[j][i] == '1'):
            c1 += 1
    out += "1" if c1>c0 else "0"
print (int(out, 2)*(int(out,2)^4095))
