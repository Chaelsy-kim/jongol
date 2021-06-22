n=int(input())
arr = [[0 for col in range(n)] for row in range(n)]
num=1
x=0
y=0
m=n

for i in range(n):
    if(i%2==0):
        y=i+1
        x=-1
    else:
        x=i+1
        y=-1
    for j in range(i+1):
        if(i%2==0):
            x+=1
            y-=1
            arr[x][y]=num
            num+=1
        else:
            x-=1
            y+=1
            arr[x][y]=num
            num+=1
if(n%2==0):
    a=y
    b=y
else:
    a=x
    b=x
 
for i in range(n-1):
    if(m%2==0):
        x=i+1
        y=b
    else:
        y=i+1
        x=a
    for j in range(n-i,1,-1):
        if(m%2==0):
            arr[x][y]=num
            num+=1
            x+=1
            y-=1   
        else:
            arr[x][y]=num
            num+=1
            x-=1
            y+=1
    m-=1
        
for i in range(n):
    for j in range(n):
        print("%d" %arr[i][j],end=' ')
    print("") 