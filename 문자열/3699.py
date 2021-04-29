a=int(input())
x=0
sum=1

for i in range(a):
    b=int(input())
    s=[0 for _ in range(b)]
    n = [[0 for col in range(20)] for row in range(b)]
    for j in range(b):
        n[j]=input().split()
    for i in range(b):
        x=n[i][1]
        if(n[i][1]==0):
            continue
        s[i]+=1
        for j in range(i+1,b):
            if(x==n[j][1]):
                s[i]+=1
                n[j][1]=0
    for i in range(b):
        if(s[i]==0):
            continue
        sum*=s[i]+1
    print(sum-1)
    sum=1


    
        
    