def majority(a):
    dict={}
    for i in a:
        dict[i]=dict.get(i,0)+1
     
    for key,value in dict.items():
        if value >len(a)/2:
            return key
    return -1
a=[2,3,4,5,2,2,2,2]
ele=majority(a)
print(ele)