n = [list(input().split()) for _ in range(5)]
list1=[0 for i in range(4)]
list2=[0 for i in range(10)]
k=0
x=0
y=0
a=0
score=0

for i in range(5):
    if(n[i][0]=='R'):
        list1[0]+=1
    elif(n[i][0]=='B'):
        list1[1]+=1
    elif(n[i][0]=='Y'):
        list1[2]+=1
    elif(n[i][0]=='G'):
        list1[3]+=1

for i in range(5):
    list2[ord(n[i][1])-ord('0')]+=1
     
for i in range(10):
    if(list2[i]!=0):
        first=i
        break
    
for i in range(10):
    if(list2[i]!=0):
        max=i
    
for i in range(first,first+5):
    if(i==10):
        break
    if(list2[i]!=0):
        k+=1
        
for i in range(10):
    if(list2[i]==4):
        score=800+i
    elif(k==5):
        score=500+max
    elif(list2[i]==3):
        score=400+i
    elif(list2[i]==2):
        score=200+i
    if(list2[i]==2):
        x+=1
        a=i
    if(list2[i]==3):
        y+=1

for i in range(4):
    if(list1[i]==5 and k==5):
        score=900+max
    elif(list1[i]==5):
        score=600+max  
      
if(x==1 and y==1):
    score=0
    for i in range(10):
        if(list2[i]==3):
            score+=i*10
        if(list2[i]==2):
            score+=i
    score+=700

elif(x==2):
    for i in range(10):
        if(list2[i]==2):
            score=i
            break
    score+=(a*10+300)
        
if(score==0):
    score=max+100
        
print(score)
  
        

            
            
        
            
        
        


    