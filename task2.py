import homework.utils


def getFiboList(size):
    fiboList = []
    for i in range(1, size + 1):
        fiboList.append(homework.utils.getFiboMoivreBinet(i))
    return fiboList


fiboList = getFiboList(1000)
print(fiboList[999])
