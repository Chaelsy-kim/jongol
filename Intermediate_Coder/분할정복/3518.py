n=int(input())
a = list(map(int,input().split()))
low=0
high=n-1
pivot=a[high]
temp=0
    
def quickSort(low,high):
    x=low
    pivot=a[high]
    if(low<high):
        for i in range(low,high):
            if(a[i]<pivot):
                temp=a[x]
                a[x]=a[i]
                a[i]=temp
                x+=1
        temp=a[x]
        a[x]=pivot
        a[high]=temp 
        for i in range(n):
            print("%d " %a[i],end='')
        print('')
        quickSort(low,x-1)
        quickSort(x+1,high)
        
quickSort(low,high)
        
