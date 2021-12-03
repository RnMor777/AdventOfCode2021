f = open("Day3.txt", "r")
arr = f.readlines()
out = ""
oxy = [x for x in arr]
co2 = [x for x in arr]
i = 0

while (len(oxy)!=1 or i==len(arr)-1):
    c0, c1 = 0, 0
    for j in range(len(oxy)):
        if (oxy[j][i] == '0'):
            c0 += 1
        elif (oxy[j][i] == '1'):
            c1 += 1
    most = '1' if c1>=c0 else '0'
    tmp = [oxy[x] for x in range(len(oxy)) if oxy[x][i]==most]
    oxy = [x for x in tmp]
    i += 1

i = 0
while (len(co2)!=1 or i==len(arr)-1):
    c0, c1 = 0, 0
    for j in range(len(co2)):
        if (co2[j][i] == '0'):
            c0 += 1
        elif (co2[j][i] == '1'):
            c1 += 1
    lest = '1' if c1<c0 else '0'
    tmp = [co2[x] for x in range(len(co2)) if co2[x][i]==lest]
    co2 = [x for x in tmp]
    i += 1

print (int(co2[0], 2)*(int(oxy[0],2)))
