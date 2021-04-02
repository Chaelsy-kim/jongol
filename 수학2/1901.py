import math
n=int(input())
arr=[0]*n
for i in range(n):
    arr[i]=int(input())
num1=0
num2=0
k=0
result=[[0]*2 for _ in range(n)]

for i in range(n):
    num1=arr[i]
    num2=arr[i]
    while(result[i][0]==0 or result[i][1]==0):
        k=0
        for j in range(2,int(math.sqrt(num1)+1)):
            if(num1%j==0):
                k+=1
                num1+=1
                break
        if(k==0):
            result[i][0]=num1
        for j in range(2,int(math.sqrt(num2)+1)):
            if(num2%j==0):
                k+=1
                num2-=1
                break
        if(k==0):
            result[i][1]=num2
    if(arr[i]-result[i][1]<result[i][0]-arr[i]):
        print("%d " %result[i][1])
    elif(arr[i]-result[i][1]>result[i][0]-arr[i]):
        print("%d " %result[i][0])
    else:
        if(result[i][0]==0 or result[i][1]==0):
            continue
        elif(result[i][0]==result[i][1]):
            print("%d" %result[i][0])
        else:
            print("%d %d" %(result[i][1],result[i][0]))
        


        
    
