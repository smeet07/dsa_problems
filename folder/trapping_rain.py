import sys
def trap(a):
    left=[0]*len(a)
    water=0
    for i in range(1,len(a)-1):
        left[i]=max(left[i-1],a[i-1])
    right=-sys.maxsize-1
    for i in reversed(range(1,len(a)-1)):
        right=max(right,a[i+1])
        if min(left[i],right)>a[i]:
            water+=min(left[i],right)-a[i]
    print(water)
a=[7, 0, 4, 2, 5, 0, 6, 4, 0, 5]
trap(a)