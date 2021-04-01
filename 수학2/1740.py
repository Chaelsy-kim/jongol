import math
m=int(input())
n=int(input())
sum=0
k=0
x=0
num=0

for i in range(m,n+1):
    k=0
    for j in range(2,int(math.sqrt(i))+1):
        if(i%j==0):
            k+=1
            break
    if(k==0):
        x+=1
        sum+=i
    if(x==1):
        num=i
        x+=1
if(m==1):
    num=2
    sum-=1       
if(x==0):
    print(-1)
else:
    print(sum)
    print(num)
    
        
