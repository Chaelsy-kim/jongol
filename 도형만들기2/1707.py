n=int(input())
arr = [[0 for col in range(n)] for row in range(n)]
num=1
x=0
y=-1
a=n-1
b=0
c=a 
m=int(n/2)

for i in range(m):
    for j in range(c*2+1):
        if(y<a):
            y+=1
        elif(x<a):
            x+=1
        arr[x][y]=num
        num+=1
    for j in range(c*2-1):
        if(y>b):
            y-=1
        elif(x>b):
            x-=1
        arr[x][y]=num
        num+=1
    a-=1
    c-=2
    b+=1

if(n%2!=0):
    arr[m][m]=num
    
for i in range(n):
    for j in range(n):
        print("%d " %arr[i][j],end='')
    print("")        