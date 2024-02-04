import math


def getFiboClassic(n):
    fibo1 = 1
    fibo2 = 1
    for i in range(2, n):
        fibo3 = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibo3

    return fibo2


def getFiboMoivreBinet(n):
    return round(((((1+math.sqrt(5))/2)**n)
                 - (((1-math.sqrt(5))/2)**n))/math.sqrt(5))
