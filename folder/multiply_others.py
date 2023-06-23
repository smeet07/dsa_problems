def multiply(a):
    left=[0]*len(a)
    right=[None]*len(a)
    index=[None]*len(a)
    left[0]=1
    right[len(a)-1]=1
    for i in range(1,len(a)):
        left[i]=left[i-1]*a[i-1]
    for i in reversed(range(len(a)-1)):
        right[i]=right[i+1]*a[i+1]
    for i in range(len(a)):
        index[i]=left[i]*right[i]
    return index
a=[4,5,6,1,2]
s=multiply(a)
print(s)