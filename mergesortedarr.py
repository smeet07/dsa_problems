def merge(a,b):
    m=len(a)
    n=len(b)
    for i in range(m):
        if a[i]>b[0]:
            temp=a[i]
            a[i]=b[0]
            b[0]=temp
            first=b[0]
            j=1
            while j<n and b[j]<first:
                b[j-1]=b[j]
                j=j+1
            b[j-1]=first
a=[2,5,6]
b=[1,4,5]
merge(a,b)
print(a)
print(b)