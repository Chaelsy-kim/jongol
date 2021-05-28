n=int(input())
a=[int(input()) for i in range(n)]
a.insert(0,0)
sum=0
k=[0 for i in range(n+1)]
ans=[0 for i in range(n+1)]

def find(x):
    if(k[x]==3):
        return
    k[x]+=1
    find(a[x])
    
for i in range(1,n+1):
    find(a[i])
    for i in range(1,n+1):
        if(k[i]==3):
            ans[i]=1
    k=[0 for i in range(n+1)]
    
for i in range(1,n+1):
    if(ans[i]==1):
        sum+=1
print(sum)

for i in range(1,n+1):
    if(ans[i]==1):
        print("%d" %i)