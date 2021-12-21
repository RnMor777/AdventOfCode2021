def recurPacket (binStr, place, totSum):
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
        return place, totSum+version
    else:
        length = binStr[place]
        place += 1
        if (length == "0"):
            totLength = int(binStr[place:place+15], 2)
            place += 15
            p, ts = recurPacket(binStr, place, totSum)
            while (p-place < totLength):
                p, ts = recurPacket(binStr, p, ts)
            return p, ts+version
        else:
            numberSub = int(binStr[place:place+11], 2)
            place += 11
            p, ts = recurPacket(binStr, place, totSum)
            for i in range (numberSub-1):
                p, ts = recurPacket(binStr, p, ts)
            return p, ts+version
    return "error"


f = open("Day16.txt", "r")
h = f.read().strip()
fullStr = bin(int(h, 16))[2:].zfill(len(h) * 4)
p, ts = recurPacket(fullStr, 0, 0)
print (ts)
