def Sum(lo,hi):
    result=lo
    i=hi
    l=lo
    a=1
    while l<i:
        l+=1
        result+=l
    return result

def prog(a):
    total=0
    b=1
    for i in range(b,a/2):
        print b
        b+=2
    return b

def small(x,y,z):
    if (x<y and x<z):
        min=x
        print min
    if (y<x and y<z):
        min=y
        print min
    if (z<y and z<x):
        min=z
        print min
    if(x==y and x<z):
        min=x
        print min
    if(x==z and y<z):
        min=y
        print min
    if(z==y and x<y):
        min=x
        print min
    if(z==y and y<x):
        min=y
        print min
    if(x==z and x<z):
        min=x
        print min
    if(x==z and x==z):
        min=x
        print min
