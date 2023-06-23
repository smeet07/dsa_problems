import sys
def  difference(a):
    min=sys.maxsize
    diff=-sys.maxsize-1
    for i in range(len(a)):
        if a[i]<min:
            min=i
        if min<i and a[i]-a[min]>diff:
            diff=a[i]-a[min]
    return diff
a=[1,4,5,2,7,9]
s=difference(a)
print("maximum difference is ",s)