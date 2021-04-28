n=0
k=0
t=0
while(1):
    a=input().split()
    if(a[0]=='END'):
        break
    x=[0 for i in range(len(a))]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if(a[i]>a[j]):
                n=a[i]
                a[i]=a[j]
                a[j]=n
    for i in range(len(a)):
        if(a[i]==0):
            continue
        k=a[i]
        x[i]+=1
        for j in range(i+1,len(a)):
            if(k==a[j]):
                x[i]+=1
                a[j]=0
    for i in range(len(a)):
        if(a[i]==0):
            continue
        else:
            print("%s : %d " %(a[i],x[i]))
                
   