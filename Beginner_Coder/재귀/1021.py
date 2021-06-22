n=int(input())
m=int(input())
ans=[0 for i in range(n+1)]
a=[[0 for i in range(n+1)] for j in range(n+1)] 
for i in range(m):
    x,y,k=map(int,input().split())
    a[x][y]=k
    
for i in range(n+1):
    s=0
    for j in range(n+1):
        if(a[i][j]!=0):
            s+=1
    if(s==0):
        a[i][i]=1

def find(x,y):
    for i in range(n+1):
        if(a[x][i]!=0):
            if(i==x):
                ans[i]+=y
                return
            find(i,y*a[x][i])
find(n,1)
for i in range(n+1):
    if(ans[i]!=0):
        print("%d %d" %(i,ans[i]))


    
            
