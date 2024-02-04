def getFiboRecursive(n):
    if n in (1, 2):
        return 1
    return getFiboRecursive(n - 1) + getFiboRecursive(n - 2)
