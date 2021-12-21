def prod(arr):
    x = 1
    for i in arr:
        x *= i
    return x

def recurPacket (binStr, place):
    version = int(binStr[place:place+3], 2)
    ID = int(binStr[place+3:place+6], 2)
    place += 6

    if (ID == 4):
        numb = ""
        while (binStr[place]!='0'):
            numb += binStr[place+1:place+5]
            place += 5
        numb += binStr[place+1:place+5]
        place += 5
        return place, int(numb, 2)
    else:
        length = binStr[place]
        retArr = []
        place += 1
        p = 0
        if (length == "0"):
            totLength = int(binStr[place:place+15], 2)
            place += 15
            p, ts = recurPacket(binStr, place)
            retArr.append(ts)
            while (p-place < totLength):
                p, ts = recurPacket(binStr, p)
                retArr.append(ts)
        else:
            numberSub = int(binStr[place:place+11], 2)
            place += 11
            p, ts = recurPacket(binStr, place)
            retArr.append(ts)
            for i in range (numberSub-1):
                p, ts = recurPacket(binStr, p)
                retArr.append(ts)
        
        if (ID==0):
            return p, sum(retArr)
        elif (ID==1):
            return p, prod(retArr)
        elif (ID==2):
            return p, min(retArr)
        elif (ID==3):
            return p, max(retArr)
        elif (ID==5):
            return p, 1 if retArr[0]>retArr[1] else 0
        elif (ID==6):
            return p, 1 if retArr[0]<retArr[1] else 0 
        elif (ID==7):
            return p, 1 if retArr[0]==retArr[1] else 0 
    return "error", "error"


f = open("Day16.txt", "r")
h = f.read().strip()
fullStr = bin(int(h, 16))[2:].zfill(len(h) * 4)
p, ts = recurPacket(fullStr, 0)
print (ts)
