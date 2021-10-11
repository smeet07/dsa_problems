def swap(a,b):
    temp=a
    a=b
    b=temp

def highlow(a):
    if len(a)%2==0:
        i=1
    else:
        i=0
    while i<len(a)-1:
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
        i+=2
    return a

a=[9,3,4,5,6,7,8]
a.sort()
s=highlow(a)
print(s)
