n=int(input())
arr = [[0 for col in range(n)] for row in range(n)]
num=1
a=int(n/2)
x=0
y=a
arr[x][y]=num
num+=1

for i in range(n*n-1):
    if((num-1)%n==0):
        x+=1
    else:
        if(x-1<0):
            x=n-1
            y-=1
        elif(y-1<0):
            x-=1
            y=n-1
        else:
            x-=1
            y-=1
    arr[x][y]=num
    num+=1
        
for i in range(n):
    for j in range(n):
        print("%d" %arr[i][j],end=' ')
    print("") 
