def equi(a):
    left=[0]*len(a)
    right=0
    index=[]
    for i in range(1,len(a)):
        left[i]=left[i-1]+a[i-1]
    for i in reversed(len(a)):
        if left[i]==right:
            index.append(i)
        right+=a[i]
    return index

a=[-2,3,4,7,5]
s= equi(a)
print(s)
