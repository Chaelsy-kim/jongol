a,b=map(int,input().split())

while (a<2 or a>9) or (b<2 or b>9):
    print("INPUT ERROR!")
    a,b=map(int,input().split())


if a<b:
    for j in range(1,10):
        for i in range(a,b+1):
            print("%d * %d = %2d   " %(i,j,i*j),end='')
        print(" ")

else:
    for j in range(1,10):
        for i in range(a,b-1,-1):
            print("%d * %d = %2d   " %(i,j,i*j),end='')
        print(" ")
    


