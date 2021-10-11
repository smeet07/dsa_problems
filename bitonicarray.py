def bitonic(a):
    left=[1]*len(a)
    for i in range(1,len(a)):
        if a[i]>a[i-1]:
            left[i]=left[i-1]+1
    right=[1]*len(a)
    for i in reversed(range(len(a)-1)):
        if a[i]>a[i-1]:
            right[i]=right[i-1]+1
    max=1
    start,end=0,0
    for i in range(len(a)):
        if max<left[i]+right[i]-1:
            max=left[i]+right[i]-1
            start=i-left[i]+1
            end=i+right[i]-1

    print("length is ",max)
    print("start and and are",a[start:end+1])

    
    

    
             

a=[1,2,4,3,5,6]
bitonic(a)