a=int(input())
b=int(input())

result=0
k=1
arr1=[a%10,int(a/10)%10,int(a/100)]
arr2=[b%10,int(b/10)%10,int(b/100)]


for j in range(0,3):
    num=1
    sum=0
    for i in range(0,3):
        sum+=num*arr1[i]*arr2[j]
        num*=10
    print(sum)
    result+=sum*k
    k*=10
print(result)

"""
print(a*(b%10))
print(a*(int(b/10)%10))
print(a*int(b/100))
print(a*b)
"""
