import SpiralMatrixGeneratorA

myInput = 289326

myField = SpiralMatrixGeneratorA.genField(myInput, 1, 's', 1)


def defCo(input0):
    myRow = 0
    rows = myField.splitlines()
    founded = False
    while founded is False:
        splitted = rows[myRow].split()
        if input0 in splitted:
            y = myRow
            x = splitted.index(input0)
            founded = True
        else:
            myRow += 1

    return x, y


def calcDis(input1, input2):
    input1, input2 = str(input1), str(input2)

    xco1, yco1 = defCo(input1)[0], defCo(input1)[1]
    xco2, yco2 = defCo(input2)[0], defCo(input2)[1]

    xDis = abs(xco1 - xco2)
    yDis = abs(yco1 - yco2)

    totDis = xDis + yDis

    return totDis


steps = calcDis(myInput, 1)
print("\n")
print("It takes %d steps from %d to the center (1)." % (steps, myInput))
