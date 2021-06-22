n=int(input())
a = [list(map(int,input().split())) for _ in range(n)]
num1=[0 for i in range(3)]
num2=[0 for i in range(3)]
ans=0

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if(i==j or j==k or k==i):
                continue
            sum=0
            num1[0]=i
            num1[1]=j
            num1[2]=k
            for s in range(n):
                strike=0
                ball=0
                num2[0]=a[s][0]//100
                num2[1]=(a[s][0]%100)//10
                num2[2]=a[s][0]%10
                for x in range(3):
                    for y in range(3):
                        if(x==y):
                            if(num1[x]==num2[y]):
                                strike+=1
                        else:
                            if(num1[x]==num2[y]):
                                ball+=1
                if(strike==a[s][1] and ball==a[s][2]):
                    sum+=1
                else:
                    break
            if(sum==n):
                ans+=1

print(ans)
                
                    
                    
    