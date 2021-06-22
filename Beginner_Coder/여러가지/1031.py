n = [[0 for col in range(5)] for row in range(5)]
m = []

for i in range(5):
    n[i]=input().split()
for i in range(5):
    m.extend(input().split())

x=True
for i in range(25):
    sum=0
    for j in range(5):
        for k in range(5):
            if(n[j][k]==m[i]):
                n[j][k]=0
                break
        if(n[j][k]==m[i]):
            break
    for j in range(5):
        s=0
        for k in range(5):
            if(n[j][k]==0):
                s+=1
        if(s==5):
            sum+=1
        if(sum==3):
            print(i+1)
            x=False
            break
    if(x==False):
        break
    for j in range(5):
        s=0
        for k in range(5):
            if(n[k][j]==0):
                s+=1
        if(s==5):
            sum+=1
        if(sum==3):
            print(i+1)
            x=False
            break
    if(x==False):
        break   
    s=0        
    for j in range(5):
        if(n[j][j]==0):
            s+=1
    if(s==5):
        sum+=1
        if(sum==3):
            print(i+1)
            x=False
            break
    if(x==False):
        break  
    s=0          
    for j in range(5):
        if(n[4-j][j]==0):
            s+=1
    if(s==5):
        sum+=1
        if(sum==3):
            print(i+1)
            x=False
            break
    if(x==False):
        break
            
            
