import homework.utils


def getFiboList(size):
    fiboList = []
    for i in range(1, size):
        fiboList.append(homework.utils.getFiboClassic(i))
    return fiboList


fiboList = getFiboList(5000)
print(fiboList[999])
