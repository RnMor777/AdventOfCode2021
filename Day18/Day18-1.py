import math, re

def xsplit (curr):
    numbs = list(map(int, curr.replace('[', '').replace(']', '').split(',')))
    splitindex = [x for x in numbs if x > 9]

    if (len(splitindex) > 0):
        maxnumb = splitindex[0]
        maxindex = numbs.index(maxnumb)
        low, high = math.floor(maxnumb/2), math.ceil(maxnumb/2)
        currindex = curr.index(str(maxnumb))
        curr = curr[:currindex] + '['+str(low)+','+str(high)+']' + curr[currindex+2:]
        return curr, 1

    return curr, 0

def explode (curr):
    nest = 0
    pos = 0
    numbs = list(map(int, curr.replace('[', '').replace(']', '').split(',')))
    for i in range(len(curr)):
        if (curr[i] == "["):
            nest += 1
        elif (curr[i] == "]"):
            nest -= 1
        elif (curr[i] == ","):
            pos += 1

        # explodes
        if (nest == 5):
            if (pos > 0):
                numbs[pos-1] += numbs[pos]
            if (pos+2 < len(numbs)):
                numbs [pos+2] += numbs[pos+1]
            numbs[pos] = 0
            numbs.pop(pos+1)
            x = i
            while (curr[x] != ']'):
                x += 1
            curr = curr[:i] + '0' + curr[x+1:]

            # sets the new string
            newcurr = ""
            pos = 0
            skipnext = 0
            for i in curr:
                if (i.isnumeric() and skipnext==0):
                    newcurr += str(numbs[pos])
                    pos += 1
                    skipnext = 1
                elif (not i.isnumeric()):
                    newcurr += i
                if (i == ','):
                    skipnext = 0
            return newcurr, 1
    return curr, 0

f = open("Day18.txt", "r")
arr = f.readlines()
curr = arr[0].strip()

for i in arr[1:]:
    curr = "[" + curr + "," + i.strip() + "]"
    while (True):
        retVal1, retVal2 = 1, 1
        while (retVal1 == 1):
            curr, retVal1 = explode(curr)
        curr, retVal2 = xsplit(curr)
        if (retVal1==0 and retVal2==0):
            break

x = re.findall("\[\d+,\d+\]", curr)
while (len(x)!=0):
    for i in x:
        l, r = list(map(int, i.replace("[","").replace("]","").split(',')))
        tmpstr = "\["+str(l)+','+str(r)+'\]'
        curr = re.sub(tmpstr, str(3*l+2*r), curr)
    x = re.findall("\[\d+,\d+\]", curr)
print (curr)
