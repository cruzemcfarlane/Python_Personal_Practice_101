def add_loop():
    num1=0
    sum1=0
    while num1<10:
        num1=num1+1
        print num1

def larger(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

    
def abder():
    num1=0
    for count in range(1,11):
        num1=num1+1
    return num1

def fac(num):
    beta=0
    if num<=1:
        return 1
    else:
        return num*fac(num-1)
    
