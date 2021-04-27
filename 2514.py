a=input()
sum1=0
sum2=0

for i in range(len(a)-2):
    if(a[i]=='K'):
        if(a[i+1]=='O' and a[i+2]=='I'):
            sum1+=1
    elif(a[i]=='I'):
        if(a[i+1]=='O' and a[i+2]=='I'):
            sum2+=1

print(sum1)
print(sum2)
    