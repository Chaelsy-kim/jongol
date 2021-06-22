arr=list(input())
sum=0
num=0

for i in range(len(arr)):
    num=int(arr[i])
    for j in range(len(arr)-i-1,0,-1):
        num*=2
    sum+=num

"""
for i in range(len(arr)):
    sum=2*sum+int(arr[i])
"""

print(sum)