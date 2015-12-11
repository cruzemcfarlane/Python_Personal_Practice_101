def sortation(mix):
    a=0
    b=1

    ac=0
    bd=1
    
    temp=0

    while not len(mix):
        if mix[a]>mix[b]:
            mix[ac]=mix[a]
            mix[bd]=mix[b]
            
            temp=mix[b]
            mix[b]=mix[a]
            mix[a]=temp

            a+=1
            b+=1
        elif mix[a]==mix[b]:
            a=+1
            b=+1
        else:
            mix[ac]=mix[a]
            mix[bd]=mix[b]
            
            temp=mix[a]
            mix[a]=mix[b]
            mix[b]=temp

            a+=1
            b+=1
