import sys

n=int(input())
m=int(n/2)
a=m
if(n>100 or n%2==0):
    print("INPUT ERROR!")
    sys.exit()
    
for i in range(n):
    if(i<m):
        for j in range(i):
            print(" ",end='')
        for k in range(2*i+1):
            print("*",end='')
    else:
        for j in range(m):
            print(" ",end='')
        for k in range(2*m+1):
            print("*",end='')
        m-=1
    print("")

"""
a=0
b=1
for i in range(n):
    for j in range(a+b):
        if(j<a):
            print(" ",end='')
        else:
            print("*",end='')
    if(i<m):
        a+=1
        b+=2
    else:
        a-=1
        b-=2
    print("")
"""
        
        
