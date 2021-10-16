import sys
def replace(a,k):
    sum=0

    left=0
    right=0
    window=0

    for i in range(len(a)):
        sum+=a[i]
        
        if sum>k:
            sum=sum-a[left]
            left=left+1
            if sum==k:
                
                right=i
                window=left
            
            

            
    return window,right
a=[2, 6, 0, 9, 7, 3, 1, 4, 1, 10]
k=15
left,right=replace(a,k)
print('window is from ',(left,right))
