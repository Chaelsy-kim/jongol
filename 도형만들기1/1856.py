a,b=map(int,input().split())
num=1
matrix = [[0 for col in range(b)] for row in range(a)]

for i in range(0,a):
    for j in range(0,b):
        if(i%2==0):
            matrix[i][j]=num
        else:
            matrix[i][b-j-1]=num
        num+=1

for i in range(0,a):
    for j in range(0,b):
        print("%d" %matrix[i][j],end=' ')
    print(" ")
  
