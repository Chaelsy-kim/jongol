a=int(input())
n = [list(map(int,input().split())) for _ in range(a)]
sum=100*100
m=0
for i in range(1,101):
    for j in range(1,101):
        m=0
        for k in range(a):
            x=n[k][0]
            y=n[k][1]
            if(i>=x and i<x+10 and j>=y and j<y+10):
                m+=1
        if(m==0):
            sum-=1
    

print(sum)
    
