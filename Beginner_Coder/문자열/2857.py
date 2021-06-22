a = [[-1 for col in range(15)] for row in range(5)]
a[0]=list(input())
a[1]=list(input())
a[2]=list(input())
a[3]=list(input())
a[4]=list(input())

for i in range(5):
    for j in range(len(a[i]),15):
        a[i].append(-1)

for i in range(15):
    for j in range(5):
        if(a[j][i]==' ' or a[j][i]==-1):
            continue
        else:
            print(a[j][i],end='')