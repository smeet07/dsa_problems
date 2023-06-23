a=list(map(int,input().split()))
target=int(input())
n=len(a)
a.sort()
low,high=(0,n-1)
while low<high:

    if a[low]+a[high]==target:
        print('sum found',a[low],a[high])
        break
    if a[low]+a[high]<target:
        low=low+1
    else:
        high=high-1
