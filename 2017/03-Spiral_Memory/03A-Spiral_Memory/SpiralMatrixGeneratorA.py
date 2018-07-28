import math


def genField(integer, type, joinmethod, space):

    def findCorner(myInt):
        mySqrt = math.sqrt(float(myInt))
        while mySqrt != int(math.ceil(mySqrt)):
            myInt += 1
            mySqrt = math.sqrt(float(myInt))
        return myInt, int(mySqrt)

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

    dirs = [
        ('right', 0, -1, 1, 0),
        ('up', -1, 0, 0, -1),
        ('left', 0, 1, -1, 0),
        ('down', 1, 0, 0, 1)
        ]

    corner, side = findCorner(integer)
    if type == 1:
        myList = range(1, integer + 1)
    elif type == 2:
        myList = range(integer + 1)
        corner, side = findCorner(corner + 1)
    elif type == 3:
        myList = range(integer)
    elif type == 4:
        myList = range(1, corner + 1)
    else:
        myList = range(corner)

    myList = range(1, corner + 1)

    field = genEmptyField(side)

    x = int(round(float(side) / 2 - 1))
    y = int(side / 2)

    dir = dirs[3][0]
    field[y][x] = myList[0]
    dir = nextDir(dir)
    x += 1
    field[y][x] = myList[1]

    for i in myList[2:]:
        if checkLeft(x, y, dir)[0]:
            x, y = frontPos(x, y, dir)
            field[y][x] = i
        else:
            x, y = checkLeft(x, y, dir)[1], checkLeft(x, y, dir)[2]
            field[y][x] = i
            dir = nextDir(dir)

    if joinmethod == "s" or joinmethod == "S":
        m = " " * space
    else:
        m = "\t"

    tempField = []
    for a in range(side):
        tempField.append((str(m.join(map(str, field[a])))).expandtabs(space))
    matrix = "\n".join(map(str, tempField))

    return matrix
