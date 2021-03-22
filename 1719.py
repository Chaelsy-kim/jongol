import sys

n,m=map(int,input().split())
y=0
p=0
if(n>100 or n%2==0 or m<1 or m>4):
    print("INPUT ERROR!")
    sys.exit()

x=int(n/2)
if(m==1):
    for i in range(n):
        if(i<x):
            for j in range(0,i+1):
                print("*",end='')
        else:
            for k in range(i,n):
                print("*",end='')
        print("")
        
elif(m==2):
    for i in range(n):
        if(i<x):
            for j in range(i,x):
                print(" ",end='')
            for j in range(0,i+1):
                print("*",end='')
        else:
            for k in range(x,i):
                print(" ",end='')
            for k in range(i,n):
                print("*",end='')
        print("")
        
elif(m==3):
    for i in range(n):
        if(i<x):
            for j in range(0,i):
                print(" ",end='')
            for j in range(n-y,0,-1):
                print("*",end='')
            y+=2
        else:
            for k in range(i,n-1):
                print(" ",end='')
            for k in range(0,(i-x)*2+1):
                print("*",end='')
        print("")
        
else:
    for i in range(n):
        if(i<x):
            for j in range(0,i):
                print(" ",end='')
            for j in range(i,x+1):
                print("*",end='')
        else:
            for k in range(0,x):
                print(" ",end='')
            for k in range(0,p+1):
                print("*",end='')
            p+=1
        print("")