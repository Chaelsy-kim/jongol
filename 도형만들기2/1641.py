import sys

n,m=map(int,input().split())
matrix = [[-1 for col in range(n*2)] for row in range(n)]
num=0
a=n
if(n>100 or n%2==0 or m>3):
    print("INPUT ERROR!")
    sys.exit()
   
if(m==1):
    for i in range(n):
        if(i%2==0):
            for j in range(i+1):
                num+=1
                matrix[i][j]=num
        else:
            for j in range(i,-1,-1):
                num+=1
                matrix[i][j]=num 
elif(m==2):
    for i in range(n):
        for j in range(i,(n-i)*2-1+i):
            matrix[i][j]=num
        num+=1
else:
    for i in range(int(n/2)+1):
        num+=1
        for j in range(i,a):
            matrix[j][i]=num
        a-=1

for i in range(n):
    for j in range(n*2):
        if(matrix[i][j]==-1):
            print("  ",end='')
        else:
            print("%d " %matrix[i][j],end='')
    print("")         
        
"""
1)
if(m==1):
    for i in range(n):    
        if(i%2==0):
            for j in range(0,i+1):
                num+=1
                print("%d " %num,end='')
        else:
            sum=0
            for j in range(0,i+1):
                sum+=1
            num+=sum
            for j in range(0,i+1): 
                print("%d " %num,end='')
                num-=1
            num+=sum
        print('')

2)
if(m==1):
    for i in range(1,n+1):
        if(i%2==0):
            num+=i
        for j in range(0,i):
            if(i%2==0):
                print("%d " %(num-j),end='')
            else:
                num+=1
                print("%d " %num,end='')
        print("")
"""

        





