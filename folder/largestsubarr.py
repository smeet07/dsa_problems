def isspossible(a,max_val,min_val,j,i):
    if max_val-min_val!=j-i:
        return False
    visited=[False]*(j-i+1)
    for k in range(i,j+1):
        if visited[a[k]-min_val]:
            return False    
        visited[a[k]-min_val]=True
    return True
def subarr(a):
    length=1
    strt=0
    end=0
    for i in a:
        min_val=a[i]
        max_val=a[i]
        j=i+1
        for j in range(len(a)):
            min_val=min(a[j],min_val)
            max_val=max(a[j],max_val)
            if isspossible(a,max_val,min_val,j,i):
                if length<max_val-min_val+1:
                    length=max_val-min_val+1
                    strt=i
                    end=j
    print("largest sub array is from pos",(strt,end))


a=[2,0,2,1,3,4]
subarr(a)