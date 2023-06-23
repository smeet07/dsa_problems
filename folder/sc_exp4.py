import math
def calfnet(lamb,net):
    temp=2/(1+math.exp(-1*lamb*net))
    return temp-1
def calfdash(out):
    temp=(1-out*out)
    return temp/2
def calcdelw(c,d1,out,fdash,x1):
    temp=c*(d1-out)*fdash
    delw=list()
    
    for i in range(0,len(x1)):
        delw.append(temp*float(x1[i]))
    return delw
x1=input("enter input vector: ").split()
d1=float(input("enter target value: "))
w1=input("enter weight vector: ").split()
c=float(input("enter learning constant: "))
lamb=float(input('enter steepness parameter: '))
net=0
for i in range(0,len(x1)):
    net=net+float(x1[i])*float(w1[i])
print("Net :",net)
out=calfnet(lamb,net)
print(out)
fdash=calfdash(out)
print(fdash)
delw=calcdelw(c,d1,out,fdash,x1)
print(delw)