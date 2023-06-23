from functools import cmp_to_key
@cmp_to_key
def custom(a,b):
    val1=str(a)+str(b)
    val2=str(b)+str(a)
    if val1>val2:
        return -1
    else:
        return 1
def customcompare(a):
    a.sort(key=custom)
    return ''.join(map(str,a))
a=[10, 68, 97, 9, 21, 12]
s=customcompare(a)
print(s)
