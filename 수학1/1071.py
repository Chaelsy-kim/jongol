a=int(input())
arr=[0]*a
arr=list(map(int,input().split()))
c=int(input())
sum1=0
sum2=0

for i in range(a):
    if(c%arr[i]==0):
        sum1+=arr[i]
    if(arr[i]%c==0):
        sum2+=arr[i]
    
print(sum1)
print(sum2)

