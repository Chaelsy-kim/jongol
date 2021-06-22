n,m=map(int,input().split())
arr = [[0 for col in range(n)] for row in range(n)]
a=1

for i in range(n):
    for j in range(i+1):
        if(j==0):
            arr[i][j]=1
        elif(i==j):
            arr[i][j]=1
        else:
            arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
            
if(m==1):  
    for i in range(n):
        for j in range(n):
            if(arr[i][j]==0):
                print("  ",end='')
            else:
                print("%d " %arr[i][j],end='')
        print("") 
elif(m==2):
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            if(arr[i][j]==0):
                print("  ",end='')
            else:
                print("%d " %arr[i][j],end='')
        print("") 
        for k in range(a):
            print(" ",end='')
        a+=1
else:
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if(arr[j][i]==0):
                print("  ",end='')
            else:
                print("%d " %arr[j][i],end='')
        print("") 