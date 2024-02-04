import homework


def getListSum(L):
    sum = 0
    for i in L:
        sum += i
    return sum


print("Enter value")
num = int(input())

fiboList = []
i = 1

while True:
    fiboList.append(homework.getFiboClassic(i))

    if fiboList[-1] > num:
        fiboList.pop()
        break

    i += 1

zeckendorfList = [fiboList[-1]]
fiboList.pop()
fiboList.reverse()

for i in fiboList:
    currentSum = getListSum(zeckendorfList)
    if i <= (num - currentSum):
        zeckendorfList.append(i)

print(zeckendorfList)
