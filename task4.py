import math
import homework


goldenRatio = (1+math.sqrt(5))/2

for i in (10, 100, 1000, 10000, 100000):
    fibo1 = homework.getFiboClassic(i)
    fibo2 = homework.getFiboClassic(i+1)

    currentRatio = fibo2/fibo1
    absoluteError = math.fabs(currentRatio-goldenRatio)
    relativeError = absoluteError/goldenRatio

    print("The absolute error of order ", i, " is equal to ", absoluteError)
    print("The relative error of order ", i, " is equal to ", relativeError)
    print()
