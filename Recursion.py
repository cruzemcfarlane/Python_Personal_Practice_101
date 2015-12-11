def isEven(x):
    if x<=1:
        return 0
    if x%2==0:
        return 1+isEven(x-1)
    else:
        return isEven(x-1)
    return x


