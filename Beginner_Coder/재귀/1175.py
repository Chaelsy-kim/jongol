n,m=map(int,input().split())
k=[1 for i in range(n+1)]

def dice(x):
    sum=0
    if(x>n):
        for i in range(1,n+1):
            sum+=k[i]
        if(sum==m):
            for i in range(1,n+1):
                print("%d " %k[i],end='')
            print('')
        return 
    
    for i in range(1,7):
        k[x]=i
        dice(x+1)

dice(1)
        
