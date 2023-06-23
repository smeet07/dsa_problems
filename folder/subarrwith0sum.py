def insert(dict,key,value):
    dict.setdefault(key,[]).append(value)
a=list(map(int,input().split()))
dict={
}
insert(dict,0,-1)
sum=0
for i in range(len(a)):
    sum=sum+a[i]
    if sum in dict:
        list=dict.get(sum)
        for value in list:
            print('sublist found at ',(value+1,i))
    insert(dict,sum,i)


