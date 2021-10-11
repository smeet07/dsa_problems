def replace(a,k):
    count=0
    max_length=0
    left=0
    right=0
    window=0
    for i in range(len(a)):
        if a[i]==0:
            count=count+1
        while count>k:
            if a[left]==0:
                count=count-1
            left=left+1
        if i-left+1>max_length:
            max_length=i-left+1
            right=i
            window=left
    return right,window,max_length
a=[1,0,0,1,1,1,0,1,1,1]
k=1
right,window,max_length=replace(a,k)
print('window is from ',(window,right))
print('max length is ',max_length)