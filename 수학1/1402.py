a,b=map(int,input().split())
num=0

for i in range(1,a+1):
    if(a%i==0):
        num+=1
    if(num==b):
        print(i)
        break
    
if(i==a):
    print(0)
