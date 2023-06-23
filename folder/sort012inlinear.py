def sort(a,i,j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
def sorting(a):
    start=mid=0
    end=len(a)-1
    pivot=1
    while mid<=end:
        if a[mid]<pivot:
            sort(a,start,mid)
            start=start+1
            mid=mid+1
            
        elif a[mid]>pivot:
            sort(a,mid,end)
            end=end-1
        else:
            mid=mid+1
    print(a)
a=[0,1,1,1,2,0,0,1,2]
sorting(a)