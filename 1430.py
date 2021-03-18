a=int(input())
b=int(input())
c=int(input())
arr1=[]
arr2=[0]*10

result=a*b*c
while result!=0:
    arr1.append(result%10)
    arr2[result%10]+=1
    result=int(result/10)

for i in range(0,10):
    print(arr2[i])