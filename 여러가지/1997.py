D,k=map(int,input().split())
a=[0 for i in range(31)]
b=[0 for i in range(31)]
a[1]=1
a[2]=0
a[3]=1
a[4]=1
b[1]=0
b[2]=1
b[3]=1

if(D!=3):
    for i in range(5,D+1):
        a[i]=a[i-2]+a[i-1]
    for i in range(4,D+1):
        b[i]=b[i-2]+b[i-1]
    
m=True
for x in range(1,1000):
    for y in range(1,1000):
        if(a[D]*x+b[D]*y==k):
            if(x>y):
                continue
            print(x)
            print(y)
            m=False
            break
    if(m==False):
        break
        