n,p=map(int,input().split())
m=[0 for i in range(100)]
sum=0

def cal(a,b,c):
    ans=(a*b)%c
    m[ans]+=1
    for i in range(100):
        if(m[i]==3):
            return
    cal(ans,b,c)
    
x=(n*n)%p
m[x]+=1
cal(x,n,p)
for i in range(100):
    if(m[i]>1):
        sum+=1
print(sum)
