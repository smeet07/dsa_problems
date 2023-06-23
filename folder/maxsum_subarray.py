import sys
def sub(a):
    maximum=max(a)
    if maximum<0:
        return maximum
    max_overall=0
    max_sublist=0
    for i in range(len(a)):
        max_sublist=max_sublist+a[i]
        max_sublist=max(max_sublist,0)
        max_overall=max(max_overall,max_sublist)
    return max_overall

a=[-3,0,4,5,6]
s=sub(a)
print("maximum sum is ",s)