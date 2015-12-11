def square(h):
    q=0
    i=-1
	
    while q<h:
        i=i+1
        print 'i=',i*i
        q+=i*i
        print 'q=',q
    return q

def osquare(h):
    q=-1
    i=0 
	
    while i<h:
        q=q+1
        i+=q*q
    return q,i

def tot():
    total=0
    num=0
    for k in range(1,51):
        
        total+=k*k
        print 'Num',k, 'Total',k*k
    return total

def Sum(n):
    avg=0
    k=0
    for i in range(1,n+1):
        k=k+i
    avg=(k/n)
    return avg

def ksquare(k,m):
    q=0
    f=k
    while(f<m):
        if (k**.5)%1==0:
            q+=1
        else:
            q+=0
        f+=1
    return q

def hsquare(h):
    q=0
    f=1
    while(f<h):
        if (f**.5)%1==0:
            print "Before: ",f
            q+=f
            print "After: ",q
        else:
            q+=0
        f+=1
    return q

