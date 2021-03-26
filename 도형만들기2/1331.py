n=int(input())
a=n*2-1
b=n
arr = [[0 for col in range(a)] for row in range(a)]
cha='A'
x=-1
y=n

def addChar(cha):
    if(cha=='Z'):
        cha='@'
    cha=ord(cha)
    cha+=1
    return chr(cha)  

while(b!=0):
    for j in range(b):
        x+=1
        y-=1
        arr[x][y]=cha
        cha=addChar(cha)
        
    for j in range(b-1):
        x+=1
        y+=1
        arr[x][y]=cha
        cha=addChar(cha)
        
    for j in range(b-1):
        x-=1
        y+=1
        arr[x][y]=cha
        cha=addChar(cha)
        
    for j in range(b-2):
        x-=1
        y-=1
        arr[x][y]=cha
        cha=addChar(cha)
    b-=1
    x-=1

for i in range(a):
    for j in range(a):
        if(arr[i][j]==0):
            print(" ",end='')
        else:
            print("%c" %arr[i][j],end=' ')
    print("")   
    
      
