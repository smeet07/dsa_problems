import sys
def replace(a,k):
    sum=0
    count=0
    min_count=sys.maxsize
    left=0
    right=0
    window=0

    for i in range(len(a)):
        sum+=a[i]
        count+=1
        
        while sum>k:
            if count<min_count:
                min_count=count
                right=i
                window=left
            count-=1
            sum=sum-a[left]
            left=left+1
    return window,right
a=[2, 6, 0, 9, 7, 3, 1, 4, 1, 10]
k=10
left,right=replace(a,k)
print('window is from ',(left,right))
