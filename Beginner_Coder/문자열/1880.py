a=input()
b=input()
x=0

for i in range(len(b)):
    x=ord(b[i])-ord('a')
    if(b[i]==' '):
        print(' ',end='')
    elif(x>=0 and x<=26):
        print(a[x],end='')
    else:
        x=ord(b[i])-ord('A')
        print(chr(ord(a[x])-32),end='')