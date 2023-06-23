import sys
def replace(a,k):
    sum=0
    min_sum=sys.maxsize
    left=0
    right=0
    window=0

    for i in range(len(a)):
        sum+=a[i]
        
        if i-left+1>k:
            sum=sum-a[left]
            left=left+1
            if sum<min_sum:
                min_sum=sum
                right=i
                window=left
            
            

            
    return window,right,min_sum
a=[2,4,5,1,1,2,4]
k=3
left,right,min_sum=replace(a,k)
print('window is from ',(left,right))
print('minimum sum is ',min_sum)