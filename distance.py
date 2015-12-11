def arith(distance,n):
    sum1=0
    for i in range(1,n+1,distance): 
        sum1+=i
    return sum1



def primes(n):
    is_prime=True
    if n<2:
        print True
    elif n==2:
        print is_prime
    elif n%2==0:
        print False
    else:
        for m in range(2,n):
            if n%m==0:
                print False
            else:
                print is_prime

def primer(n):
    is_prime=0
    if n<2:
        False
    elif n==2:
        is_prime
    elif n%2==0:
        False
    else:
        for m in range(3,int(n**0.5)+1,2):
            if n%m==0:
                False
            else:
                is_prime


def fib(n):
    result=1
    i=1
    prev=0

    if n==0:
        print n
    elif n==1:
        print n
    else:
        while (i<n):
            i+=1
            result,prev=result+prev,result
        return result
            
