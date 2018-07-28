def genField(integer, myType, joinmethod, space):

    def genEmptyField(size):
        myField = []
        for i in range(size):
            myField.append([''] * size)
        return myField

    def nextDir(currentDir):
        if currentDir == dirs[-1][0]:
            newDir = dirs[0][0]
        else:
            for i in dirs:
                if currentDir in i:
                    newDir = dirs[dirs.index(i) + 1][0]
        return newDir

    def checkLeft(x, y, myDir):
        busy = True
        newX = x
        newY = y
        for i in dirs:
            if myDir in i:
                newX = x + i[1]
                newY = y + i[2]
        if field[newY][newX] == '':
            busy = False
        return busy, newX, newY

    def frontPos(x, y, myDir):
        xPos = x
        yPos = y
        for i in dirs:
            if myDir in i:
                xPos = x + i[3]
                yPos = y + i[4]
        return xPos, yPos

    def newSum(x, y, size):
        xPos = x - 1
        yPos = y - 1
        sum = 0
        crnt = 0
        for a in range(3):
            for b in range(3):
                newX = xPos + b
                newY = yPos + a
                if newX >= 0 and newX < size and newY >= 0 and newY < size:
                    crnt = field[newY][newX]
                    if isinstance(crnt, int):
                        sum += crnt
        return int(sum)

    def newCircle(size, field):
        field.insert(0, [''] * (size + 2))
        for i in range(1, size + 1):
            field[i].insert(0, '')
            field[i].append('')
        field.append([''] * (size + 2))
        newSize = size + 2
        return newSize, field

    field = genEmptyField(3)
    side = len(field)
    corner = side ** 2

    startInt = 1
    maxInt = integer + 1
    if myType == 1:
        maxInt = integer
    elif myType == 2:
        maxInt = integer + 1
    elif myType == 3:
        maxInt = corner
    else:
        maxInt = corner + 1

    dirs = [
        ('right', 0, -1, 1, 0),
        ('up', -1, 0, 0, -1),
        ('left', 0, 1, -1, 0),
        ('down', 1, 0, 0, 1)
        ]

    x = int((float(side) / 2 - 1) + 0.5)  # int(i + 0.5) = python 2.7.x round()
    y = int(side / 2)

    dir = dirs[3][0]
    field[y][x] = startInt
    dir = nextDir(dir)
    x += 1
    field[y][x] = startInt

    i = 2
    while i < maxInt:       # i != field[-1][-1]

        if checkLeft(x, y, dir)[0]:
            x, y = frontPos(x, y, dir)
            field[y][x] = newSum(x, y, side)
            i = field[y][x]
        else:
            x, y = checkLeft(x, y, dir)[1], checkLeft(x, y, dir)[2]
            field[y][x] = newSum(x, y, side)
            i = field[y][x]
            dir = nextDir(dir)
        if x == y == side - 1:
            side, field = newCircle(side, field)
            x += 1
            y += 1

    if not any(isinstance(z, int) for z in field[0]):
        del field[0]
    clearFirst = False
    for v in range(side - 1):
        if field[v][0] == '':
            clearFirst = True
        else:
            clearFirst = False
            break
    if clearFirst:
        for w in range(side - 1):
            del field[w][0]
    if not any(isinstance(r, int) for r in field[-1]):
        del field[-1]

    if joinmethod == "s" or joinmethod == "S":
        m = " " * space
    else:
        m = "\t"

    tempField = []
    for a in range(len(field)):
        tempField.append((str(m.join(map(str, field[a])))).expandtabs(space))
    matrix = "\n".join(map(str, tempField))

    return matrix, i


myInput = 289326
matrix, output = genField(myInput, 1, 't', 8)
print(matrix + "\n" * 2 + str(output))
