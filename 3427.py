n=int(input())
a=list(input())
b=[]
i=0
x=0
sum1=0
sum2=0
ans=0

def Sum(s,t):
    global sum1,sum2,ans
    for i in range(s,len(b)-t,2):
        sum1+=b[i]
    for i in range(s+1,len(b)-t,2):
        sum2+=b[i]
    if(sum1>=sum2):
        ans=sum2
    else:
        ans=sum1
    
    
while(1):
    b.append(1)
    if(n-1>i):
        while(a[i]==a[i+1]):
            b[x]+=1
            i+=1
            if(i==n-1):
                break
    if(i==n-1):
        break
    i+=1
    x+=1

if(len(b)%2==0):
    Sum(1,1)
else:
    if(b[0]<b[len(b)-1]):
        Sum(0,1)
    else:
        Sum(1,0)
        
print(ans)