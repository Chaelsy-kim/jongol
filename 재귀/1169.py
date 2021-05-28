n,m=map(int,input().split())
k=[1 for i in range(n)]
a=0
def dice1(x,y):
    global n
    
    if(x==0 or y==0):
        return
    
    dice1(x-1,y)
    dice1(6,y-1)
    
    if(y!=1):
        k[n-y]+=1
        if(k[n-y]==7):
            k[n-y]=1
    else:
        k[n-1]=x
        for i in range(n):
            print("%d " %k[i],end='')
        print('')
        
def dice2(x,y):
    global n,a
    
    if(x==0 or y==0):
        return
    
    dice2(x-1,y)
    dice2(6,y-1)
    
    if(y!=1):
        k[n-y]+=1
        if(k[n-y]==7):
            k[n-y]=1
    else:
        k[n-1]=x
        for i in range(n-1):
            if(k[i]>k[i+1]):
                a+=1
        if(a==0):    
            for i in range(n):
                print("%d " %k[i],end='')
            print('')
        a=0

def dice3(x,y):
    global n,a
    
    if(x==0 or y==0):
        return
    
    dice3(x-1,y)
    dice3(6,y-1)
    
    if(y!=1):
        k[n-y]+=1
        if(k[n-y]==7):
            k[n-y]=1
    else:
        k[n-1]=x
        for i in range(n):
            for j in range(i+1,n):
                if(k[i]==k[j]):
                    a+=1
        if(a==0):    
            for i in range(n):
                print("%d " %k[i],end='')
            print('')
        a=0
    
if(m==1):
    dice1(6,n)   
elif(m==2):
    dice2(6,n)
elif(m==3):
    dice3(6,n)
    
    