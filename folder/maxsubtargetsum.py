def large(a,target):
    
    length=0
    end=-1
    for i in range(len(a)):
        target1=0
        for j in range(i,len(a)):
            target1=target1+a[j]
            if target1==target:
                if length<j-i+1:
                    length=j-i+1
                    end=j
    print('found from',(end-length+1,end))
a=[2,3,0,4,3]
target=7

            
def large2(a,target):
    dict={
    }
    dict[0]=-1
    start=-1
    ending_index=-1
    length=0
    sum=0
    for i in range(len(a)):
        sum=sum+a[i]
        if sum not in dict:
            dict[sum]=i
        
        if sum-target in dict and length<i-dict[sum-target]:
            length=i-dict[sum-target]
            ending_index=i
            starting_index=dict[sum-target]+1
            
    print('the sum is found from ',(starting_index,ending_index))
    print('the length is ',length)
large2(a,target)






    