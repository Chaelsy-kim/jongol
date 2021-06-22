n=int(input())

def find(low,high):
    while(low<=high):
        mid=(low+high)//2
        if(n==mid*mid):
            return mid
        if(n<mid*mid):
            high=mid-1
        elif(n>mid*mid):
            low=mid+1
    return mid

a=find(0,n)
if(a*a<=n):
    print(a)
else:
    print(a-1)

