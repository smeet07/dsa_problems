def distinct(a,k,subarrays,out=(),i=0):
    if k>len(a) or len(a)==0:
        return 0
    if k==0:
        subarrays.add(out)
    for j in range(i,len(a)):
        
        distinct(a,k-1,subarrays,out+(a[j],),j+1)
a=[3,5,6,7,1,0]
k=3
subarrays=set()
distinct(a,k,subarrays)
print(subarrays)
