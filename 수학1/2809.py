import math

a=int(input())
b=int(math.sqrt(a))
arr=[]
m=0

for i in range(1,b+1):
    if(a%i==0):
        arr.append(i)
        if(int(a/i)!=i):
            arr.append(int(a/i))

for i in range(len(arr)):
    for j in range(i,len(arr)):
        if(arr[i]>arr[j]):
            m=arr[i]
            arr[i]=arr[j]
            arr[j]=m

for i in range(len(arr)):
    print("%d " %arr[i],end='')
            
        
