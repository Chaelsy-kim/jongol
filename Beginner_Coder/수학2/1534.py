m,b=map(int,input().split())
y=[]

def change(n): 
    x=m
    while(x!=0):
        a=x%n
        if(a>=10): 
            i=ord('A')+a-10
            y.append(chr(i))
        else:
            y.append(a)
        x=int(x/n)
    for i in range(len(y)-1,-1,-1):
        print(y[i],end='')


if(b==2):
    change(2)
   
elif(b==8):
    change(8)

elif(b==16):
    change(16)
    
