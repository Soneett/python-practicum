import homework.utils
import time


def getFiboListClassic(size):
    fiboList = []
    for i in range(1, size + 1):
        fiboList.append(homework.utils.getFiboClassic(i))
    return fiboList


def getFiboListMoivreBinet(size):
    fiboList = []
    for i in range(1, size + 1):
        fiboList.append(homework.utils.getFiboMoivreBinet(i))
    return fiboList


begin = time.time()
getFiboListClassic(1000)
print("Time spent on calculations in the classical way: ", time.time()-begin)

begin = time.time()
getFiboListMoivreBinet(1000)
print("Time spent on calculations in the MoivreBinet way: ", time.time()-begin)
