f = open("Day8.txt", "r")
arr = f.readlines()
numbers = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
total = 0

for i in arr:
    x, y = i.split(' | ')
    xarr = list(x.strip().split(' '))
    yarr = list(y.strip().split(' '))

    letterCount = [0 for j in range(7)]
    one = [j for j in xarr if len(j)==2]
    four = [j for j in xarr if len(j)==4]
    seven = [j for j in xarr if len(j)==3]
    eight = [j for j in xarr if len(j)==7]

    for j in xarr:
        for k in j:
            letterCount[ord(k)-ord('a')] += 1

    sections = [0 for j in range(7)]
    sections[5] = chr(letterCount.index(9)+0x61)
    sections[1] = chr(letterCount.index(6)+0x61)
    sections[4] = chr(letterCount.index(4)+0x61)
    sections[0] = [j for j in list(seven[0]) if j not in list(one[0])][0]
    sections[2] = [j for j in list(one[0]) if j!=sections[5]][0]
    sections[3] = [j for j in list(four[0]) if j not in sections][0]
    sections[6] = [j for j in list('abcdefg') if j not in sections][0]

    outNum = 0
    for j in yarr:
        tmpStr = ([chr(sections.index(k)+0x61) for k in j])
        tmpStr.sort()
        outNum *= 10
        outNum += int(numbers.index(''.join(tmpStr)))
    total += outNum 
        
print (total)
