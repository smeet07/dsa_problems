def replace(a):
    count=0
    max_length=0
    prev_index=-1
    index=-1
    for i in range(len(a)):
        if a[i]==1:
            count=count+1
        else:
            count=i-prev_index
            prev_index=i
        if count>max_length:
            max_length=count
            index=prev_index
    return index,max_length




a=[0,1,1,0,1,1,0,1,1,1,1]
index,max_length=replace(a)
print("index needed to be changed is ",index)
print("the max length of the array that would be generated is ",max_length)