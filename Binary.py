
def inpi():
    number=float(input("Enter points number to be converted to binary "))
    inteeger=int(number)
    points=number-inteeger
    binary=inte(inteeger) + "."+ pointer(points)
    print(binary)


def inte(num):
    bin=''
    if num==0:
            bin='0'
    while num !=0:
        bin=str(num%2)+bin
        num=int(num/2)

    return(bin)




def pointer(points):
    t=0
    stop=False
    binpoints=''
    while stop==False and t<10:
        
        points=points*2
        if points>=1:
            binpoints=binpoints+'1'
            if points==1:
                stop=True
            points=points-1
        
        elif points<1:
            binpoints=binpoints+'0'
        if points==0:
            binpoints='0'
        t=t+1
    return(binpoints)


inpi()