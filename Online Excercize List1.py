def prac(list1):
    i=0
    b=1
    while i<len(list1):
        while b<len(list1):
            if list1[i]==list1[b]:
                return True
            else:
                b+=1
        i+=1
    return False

def bedda(list1):
    i=0
    b=1
    has_dups=True
    if list1[i]==list1[b]:
        print has_dups
    else:
        while i<len(list1):
            while b<len(list1):
                if list1[i]>list1[b] or list1[i]<list1[b]:
                    b+=1
                else:
                    print has_dups
            i+=1
        print False




def pr(s,lst):
    contains=False
    for i  in lst:
        if i not in s:
            contains = False
        else:
            contains=True
    return contains
