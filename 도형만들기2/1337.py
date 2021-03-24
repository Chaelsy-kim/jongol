n=int(input())
a=n
matrix = [[-1 for col in range(n)] for row in range(n)]
num=0
j=0
k=0
while(a>=1):
    for i in range(a):
        matrix[i+j][i+k]=num%10
        num+=1
    a-=1
    for i in range(a):
        matrix[n-k-1][n-2-i-j]=num%10
        num+=1
    a-=1
    for i in range(a):
        matrix[a+j-i][k]=num%10
        num+=1
    a-=1
    j+=2
    k+=1
    
for i in range(n):
    for j in range(n):
        if(matrix[i][j]==-1):
            print("  ",end='')
        else:
            print("%d " %matrix[i][j],end='')
    print("")    

"""
x=-1
y=-1

for i in range(n):
    for j in range(i,n):
        if(i%3==0):
            x+=1
            y+=1
        elif(i%3==1):
            y-=1
        else:
            x-=1
        matrix[x][y]=num%10
        num+=1
"""
        