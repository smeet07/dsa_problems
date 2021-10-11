import sys
def product(a):
    a.sort()
    max=-sys.maxsize
    max_neg=a[0]*a[1]
    max_pos=a[len(a)-1]*a[len(a)-2]
    if max_neg>max_pos:
        max=max_neg
    else:
        max=max_pos
    return max
a=[-5,-4,2,0,7,8]
s=product(a)
print(s)