n=int(input())
i=1
j=n
while(n>=0):
    if(n>=i):   
        n=n-i
        if(n<i):
            print(i) 
            break   
    i=i+1 


