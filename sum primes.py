def isPrime(n):
    for count in range(2,n):  
       if (n%count == 0):     
        return False                                   
    return True
    
#Question 4
def primes(a,b):
    def isPrime(n):
        for count in range(2,n):
            if (n%count == 0):
                return False
        return True
    
    for counter in range(a,b):
        if isPrime(counter):
            print counter

def countp(n):
    total=0
    a=2
    k=0

    while k<n:
        if isPrime(a)==True:
            total+=a
            print a
            a+=1
            k+=1
        else:
            a+=1
    return total


def yanz(x,y):
    x= [1,2,3]
    y=[4,5,6]
    return zip yanz(x,y) 
