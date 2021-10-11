def large2(a):
    dict={
    }
    dict[0]=-1
    start=-1
    ending_index=-1
    length=0
    sum=0
    for i in range(len(a)):
        sum+=1 if (a[i]==1) else -1
        if sum in dict:
        
            if length<i-dict[sum]:
                length=i-dict[sum]
                start=dict[sum]+1
                ending_index=i+1
        else:
            dict[sum]=i
    print(dict)
        
        
            
    print('the sum is found from ',(start,ending_index))
    print('the length is ',length)
a=[0,1,1,1,0,0,0,1,1,1]
large2(a)