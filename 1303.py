a,b=map(int,input().split())
num=1

for i in range(1,a+1):
    for j in range(1,b+1):
        print("%d " %num,end='')
        num+=1
    print(" ")