import math
arr=[0]*5
arr=list(map(int,input().split()))
a=0

for i in range(5):
    if(arr[i]<2):
        print("number one")
        continue
    k=0
    for j in range(2,int(math.sqrt(arr[i]))+1):
        if(arr[i]%j==0):
            print("composite number")
            k+=1
            break
    if(k==1):
        continue
    print("prime number")