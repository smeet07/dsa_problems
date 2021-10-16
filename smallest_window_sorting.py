import sys
def sorting(a):
    min=sys.maxsize
    max=-sys.maxsize-1
    right=left=-1
    for i in range(len(a)):
        if a[i]>max:
            max=a[i]
        if max>a[i]:
            right=i
    for i in reversed(range(len(a))):
        if min>a[i]:
            min=a[i]
        if a[i]>min:
            left=i
    print("smallest unsorted is from ",(left,right))
a=[1, 3, 2, 7, 5, 6, 4, 8]
sorting(a)
