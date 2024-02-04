import turtle
import homework


def getFiboList(size):
    fiboList = []
    for i in range(1, size + 1):
        fiboList.append(homework.utils.getFiboMoivreBinet(i))
    return fiboList


fiboList = getFiboList(30)

for i in fiboList:
    turtle.circle(i, 90)
