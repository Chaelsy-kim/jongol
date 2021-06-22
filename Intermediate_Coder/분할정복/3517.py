n=int(input())
a=list(map(int,input().split()))
q=int(input())
b=list(map(int,input().split()))
ans=[0 for i in range(q)]

def find(x,low,high):
    while(low<=high):
        mid=(low+high)//2
        if(a[mid]==x):
            return mid
        if(a[mid]>x):
            high=mid-1
        elif(a[mid]<x):
            low=mid+1
    return -1

for i in range(q):
    if(b[i]<a[0] or b[i]>a[n-1]):
        ans[i]=-1
    else:
        ans[i]=find(b[i],0,n-1)
        
for i in range(q):
    print("%d " %ans[i],end='')
    
