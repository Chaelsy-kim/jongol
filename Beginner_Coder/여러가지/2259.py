k=int(input())
n=[[0 for col in range(2)] for row in range(6)]
for i in range(6):
    n[i]=list(map(int,input().split()))
sum=0
x=0
y=0
a=0
b=0
for i in range(6):
    if(n[i][0]==4 or n[i][0]==3):
        if(n[i][1]>x):
            x=n[i][1]
        if(n[i][0]==n[(i+2)%6][0]):
            a=n[(i+1)%6][1]
    else:
        if(n[i][1]>y):
            y=n[i][1]
        if(n[i][0]==n[(i+2)%6][0]):
            b=n[(i+1)%6][1]
    

sum=(x*y-a*b)*k
print(sum)