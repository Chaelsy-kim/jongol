import math
n,m=map(int,input().split())
arr=[0 for i in range(m+1)]
sum=0

arr[0]=arr[1]=1

for i in range(2,int(math.sqrt(m))+1):
    if(arr[i]==0):
        for j in range(i*i,m+1,i):
            arr[j]=1

for i in range(n,m+1):
    if(arr[i]!=1):
        sum+=1
print(sum)