n=int(input())
sum=1

def Factorial(a):
    global sum
    sum*=a
    if(a==1):
        print("%d! = %d" %(a,a))
        return
    else:
        print("%d! = %d * %d!" %(a,a,a-1))
    Factorial(a-1)

Factorial(n)
print(sum)

    
