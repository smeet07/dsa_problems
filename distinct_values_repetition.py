def distinct(a,k,out,i):
    if k==len(out):
        print(out)
        return
    for j in range(i,len(a)):
        out.append(a[j])
        distinct(a,k,out,j)
        out.pop()
a=[2,4,5]
k=2
out=[]
distinct(a,k,out,0)