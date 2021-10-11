def distinct(a,k,out,i):
    if k>len(a) or len(a)==0:
        return 0
    if k==len(out):
        print(out)
        return 
    for j in range(i,len(a)):
        out.append(a[j])
        distinct(a,k,out,j)
        out.pop()
a=[3,5,6]
k=3
out=[]
distinct(a,k,out,0)
