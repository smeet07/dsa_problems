def circular(a):
    max_sublist=0
    max_overall=0
    for i in range(len(a)):
        max_sublist=max_sublist+a[i]
        max_sublist=max(max_sublist,0)
        max_overall=max(max_sublist,max_overall)
    return max_overall
a=[5,6,2,3,4,-3,4,6]
maximum=max(a)
if maximum<0:
    print(maximum)
for i in range(len(a)):
    a[i]=-a[i]   
neg=circular(a)
for i in range(len(a)):
    a[i]=-a[i]
max_max=max(circular(a),sum(a)+neg)
print(max_max)