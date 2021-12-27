def addInf (imageArr, pixel):
    infRows = [pixel for i in range(len(imageArr[0]))]

    for i in range(3):
        imageArr.insert(0, infRows)
        imageArr.append(infRows)

    for i in range(len(imageArr)):
        tmp = pixel*3 + ''.join(imageArr[i]) + pixel*3
        imageArr[i] = list(tmp)

    return imageArr

def reductionAlg (imageArr, key):
    newOut = []
    for i in range(len(imageArr)-2):
        newRow = []
        for j in range(len(imageArr[0])-2):
            tmp = ''.join(imageArr[i][j:j+3])
            tmp += ''.join(imageArr[i+1][j:j+3])
            tmp += ''.join(imageArr[i+2][j:j+3])

            numb = ['1' if x=='#' else '0' for x in tmp]
            newPixel = key[int(''.join(numb), 2)]
            newRow.append(newPixel)
        newOut.append(newRow)
    return newOut

def countArr (imageArr):
    count = 0
    for i in range(len(imageArr)):
        for j in range(len(imageArr[0])):
            count += 1 if imageArr[i][j]=='#' else 0
    return count

def main():
    f = open("Day20.txt", "r")
    arr = f.readlines()

    key = list(arr[0].strip())
    image = addInf([list(x.strip()) for x in arr[2:]], '.')
    image = reductionAlg(image, key)
    image = addInf(image, key[0])
    image = reductionAlg(image, key)
    print (countArr(image))

if (__name__ == "__main__"):
    main()
