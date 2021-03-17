import sys

a=int(input())
if(a<1 or a>100 or a%2==0):
    print("INPUT ERROR")
    sys.exit()
    
num='A'
matrix = [[0 for col in range(a)] for row in range(a)]
b=int(a/2)

"""
for i in range(b,-1,-1):
    for j in range(i,a-i):
        matrix[j][i]=num
"""
for j in range(0,b+1):
    for i in range(0,2*j+1):
        matrix[b-j+i][b-j]=num
        if(num=='Z'):
            num='@'
        num=ord(num)
        num+=1
        num=chr(num)
      
for i in range(0,a):
    for j in range(0,a):
        if(matrix[i][j]):
            print("%c" %matrix[i][j],end=' ')
        else:
            print(" ",end=' ')        
    print(" ")