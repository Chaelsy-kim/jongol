n=int(input())
arr = [[0 for col in range(n)] for row in range(n)]
num=1
x=0
y=0
arr[x][y]=num
num+=1

while(x!=n-1 or y!=n-1):
    if(x+1>=n or x+1<0):
        y+=1
    else:
        x+=1
    arr[x][y]=num
    num+=1
    while(1):
        if(x-1>=n or x-1<0 or y+1<0 or y+1>=n):
            break;
        x-=1
        y+=1
        arr[x][y]=num
        num+=1
    if(y+1>=n or y+1<0):
        x+=1
    else:
        y+=1
    arr[x][y]=num
    num+=1
    while(1):
        if(x+1>=n or x+1<0 or y-1<0 or y-1>=n):
            break;
        x+=1
        y-=1
        arr[x][y]=num
        num+=1
        
for i in range(n):
    for j in range(n):
        print("%d" %arr[i][j],end=' ')
    print("") 