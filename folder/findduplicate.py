def find(a):
    b=[False]*(len(a)+1)
    for i in a:
        if b[i]:
            print('duplicate found',i)
        else:
            b[i]=True
a=list(map(int,input().split()))
find(a)