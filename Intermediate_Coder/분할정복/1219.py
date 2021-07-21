x,y=map(int,input().split())
a=int(input())
b=int(input())
m=[0 for i in range(y+1)]
ans=0
t=0
max1=1
max2=1

def paper(x):
    num=a
    i=1
    while(num!=0):
        if(m[i]==1):
            i+=x-1
            num-=1
        i+=1
        if(i>max2):
            return 1
    return 0
 
for i in range(b):
    s,t=map(int,input().split())
    m[t]=1
    if(max1<s):
        max1=s
    if(max2<t):
        max2=t
 
low=max1
high=max2//a 

if(low>high):
    print(low)
else:
    while(1): 
        mid=(low+high)//2
        if(paper(mid)):
            if(paper(mid-1)==0):
                break
            high=mid-1
        else:
            if(paper(mid+1)):
                mid=mid+1
                break
            low=mid+1
    print(mid)