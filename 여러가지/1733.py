n = [[0 for col in range(19)] for row in range(19)]
for i in range(19):
    n[i]=input().split()
m=True

for i in range(19):
    for j in range(19):
        a=0
        b=0
        c=0
        d=0
        s=0
        if(n[i][j]!='0'):
            x=n[i][j]
            for k in range(1,5):
                if(j+k<=18):
                    if(n[i][j+k]==x):
                        s+=1
            if(s==4):
                if(j+4<18):
                    if(n[i][j+5]==x):
                        a=1
                if(j-1>=0):
                    if(n[i][j-1]==x):
                        a=1
            else:
                a=1
            s=0
            for k in range(1,5):
                if(i+k<=18 and j+k<=18):
                    if(n[i+k][j+k]==x):
                        s+=1
            if(s==4):
                if(i+4<18 and j+4<18):
                    if(n[i+5][j+5]==x):
                        b=1
                if(j-1>=0 and i-1>=0):
                    if(n[i-1][j-1]==x):
                        b=1
            else:
                b=1
            s=0
            for k in range(1,5):
                if(i+k<=18):
                    if(n[i+k][j]==x):
                        s+=1
            if(s==4):
                if(i+4<18):
                    if(n[i+5][j]==x):
                        c=1
                if(i-1>=0):
                    if(n[i-1][j]==x):
                        c=1
            else:
                c=1
            s=0
            for k in range(1,5):
                if(i-k>=0 and j+k<=18):
                    if(n[i-k][j+k]==x):
                        s+=1
            if(s==4):
                if(i-4>0 and j+4<18):
                    if(n[i-5][j+5]==x):
                        d=1
                if(i+1<=18 and j-1>=0):
                    if(n[i+1][j-1]==x):
                        d=1
            else:
                d=1
                
            if(a==0 or b==0 or c==0 or d==0):
                print(ord(x)-ord('0'))
                print(i+1,j+1)
                m=False
                break
            
    if(m==False):
        break

if(m==True):
    print(0)
