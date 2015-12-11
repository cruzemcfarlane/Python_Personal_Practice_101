def sum1():
    j=0
    while j<5:
        j+=j
    j=j+1
    return j

def mystery():
    def bar(x):
        return x**3

def above_freezing(w):
    return w >= 0

def print_R(x):
    result=' '
    while x>=0:
        if x%2 == 0:
            result = result +'R'
        else:
            result+='R'+'R'
        x=x-1
    return result

def come(a):
    return forth(a)

def forth(x):
    return jedi(x)+2

def jedi(x):
    return knights(3)+x

def knights(x):
    return 5+x

def horror(x):
    while (x % 2 == 0):
        x = x +1 
        return x

def product(w):
    prod = 1
    for i in range(0,w):
        prod = prod * i
    return prod
