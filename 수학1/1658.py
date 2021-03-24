a,b=map(int,input().split())

def gcd_get(a,b):
    if(b==0):
        return a
    return gcd_get(b,a%b)

gcd=gcd_get(a,b)
lcm=int(a*b/gcd)

print(gcd)
print(lcm)
