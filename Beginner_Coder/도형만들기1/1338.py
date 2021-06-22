a=int(input())
num='A'
matrix = [[0 for col in range(a)] for row in range(a)]

for i in range(0,a):
    for j in range(0,a-i-1):
        matrix[i][j]=' '
    for j in range(0,a):
        if(i+j>=a):
            break
        matrix[i+j][a-j-1]=num
        if(num=='Z'):
            num='@'
        num=ord(num)
        num+=1
        num=chr(num)
        
for i in range(0,a):
    for j in range(0,a):
        print("%c" %matrix[i][j],end=' ')
    print(" ")
