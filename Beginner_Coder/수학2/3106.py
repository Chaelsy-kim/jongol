def nTOtem(m):
    global sum
    for i in range(len(n)):
        if(ord(n[i])-ord('0')>=10):
            n[i]=ord(n[i])-ord('A')+10
        sum=m*sum+int(n[i])

def tenTOn(m): 
    x=sum
    if(x==0):
        print(0,end='')
    while(x!=0):
        y=x%m
        if(y>=10): 
            i=ord('A')+y-10
            arr.append(chr(i))
        else:
            arr.append(y)
        x=x//m
    for i in range(len(arr)-1,-1,-1):
        print(arr[i],end='')  
    print("")

while(1):
    y=input().split()
    if(int(y[0])==0):
        break
    a=y[0]
    n=y[1]
    n=list(n)
    b=y[2]
    sum=0
    arr=[]
    nTOtem(int(a))
    tenTOn(int(b))
    
