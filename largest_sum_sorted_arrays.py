def sorted(a,b):
    n=len(a)
    m=len(b)
    i=j=0
    sum_x=sum=sum_y=0
    while i<n and j<m:
        while i<n-1 and a[i]==a[i+1]:
            sum_x+=a[i]
        while j<m-1 and b[j]==b[j+1]:
            sum_y+=b[j]
        if a[i]<b[j]:
            sum_x+=a[i]
            i=i+1
        elif b[j]<a[i]:
            sum_y+=b[j]
            j=j+1
        else:
            sum+= max(sum_x,sum_y)+ a[i]
        
            i+=1
            j+=1
            sum_x=0
            sum_y=0
    while i<n:
        sum_x+=a[i]
        i+=1
    while j<m:
        sum_y+=b[j]
        j+=1
    sum+=max(sum_x,sum_y)
    print('maximum  sum is ',sum)
a=[3, 6, 7, 8, 10, 12, 15, 18, 100]
b=[1, 2, 3, 5, 7, 9, 10, 11, 15, 16, 18, 25, 50]
sorted(a,b)

        

