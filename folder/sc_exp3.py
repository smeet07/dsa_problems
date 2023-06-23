import math
v=float(input('enter value of v'))
w=float(input('enter value of w'))
i1=[0.1,0,1,0.9,0.9]
i2=[0.1,0.9,0.1,0.9]
o=[0.1,0.9,0.9,0.1]
q1,q2,dv,dw,d=0,0,0,0,0
for i in range(4):
    q1=i1[i]*v +i2[i]*v
    q1=1/(1+math.exp(-q1))
    q2=q1*w*2
    q2=1/(1+math.exp(-q2))
    print('output from ',i+1,'input',q2)
    if q2==(o[i]-0.1) or q2==(o[i]+0.1):
        print('no change required')
    d=(o[i]-q2)*q1*(1-q1)
    dv=i1[i]*d+i2[i]*d
    v=v+dv
    print('change in weight hidden is ',v)
    d=(o[i]-q2)*q2*(1-q2)
    dw=q1*d*2
    w=w+dw
    print('change in weight(output)',w)
    print('--------------------------')
