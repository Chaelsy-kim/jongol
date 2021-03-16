a,b=map(int,input().split())
num=1
matrix = [[0 for col in range(a)] for row in range(a)]

if(b==1):
    for i in range(0,a):
        for j in range(0,a):
            matrix[i][j]=num
        num+=1
        
elif(b==2):
    for i in range(0,a):
        for j in range(0,a):
            if(i%2==0):
                matrix[i][j]=num
            else:
                matrix[i][a-j-1]=num
            num+=1
        num=1

else:
    for i in range(0,a):
        for j in range(0,a):
            num=(i+1)*(j+1)
            matrix[i][j]=num
    
for i in range(0,a):
    for j in range(0,a):
        print("%d" %matrix[i][j],end=' ')
    print(" ")
  
