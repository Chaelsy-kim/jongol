import sys

for i in range(10):
    n=int(input())
    if(n==0):
        sys.exit()
    a=n
    num=0
    arr=[]
    sum=0
    while(a!=0):
        if(a%10==0 and num==0):
            num-=1
        else:
            arr.append(a%10)
        a=int(a/10)
        num+=1
    
    for i in range(num):
        sum+=arr[i]
        
    for i in range(num):
        print("%d" %arr[i],end='')
        
    print(" %d" %sum)



