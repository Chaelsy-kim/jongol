a=int(input())
arr=[0]*a
arr=list(map(int,input().split()))


def gcd_get(a,b):
    if(b==0):
        return a
    return gcd_get(b,a%b)

gcd=lcm=arr[0]

for i in range(1,a):
    gcd=gcd_get(gcd,arr[i])
    lcm=int(arr[i]*lcm/gcd_get(lcm,arr[i]))

print(gcd,lcm)
