a=int(input())
num=1
matrix = [[0 for col in range(a)] for row in range(a)]


for j in range(0,a):
    for i in range(0,a):
        matrix[i][j]=num
        num+=1

for i in range(0,a):
    for j in range(0,a):
        print("%d" %matrix[i][j],end=' ')
    print(" ")
