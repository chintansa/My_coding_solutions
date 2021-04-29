n = int(input().strip())
c = list(map(int, input().rstrip().split()))


def jumpingOnClouds(c):
    count=0
    i=2
    # for i in range(0,len(c),2):
    while(i < len(c)):
    
       # print(i,count)
        if(c[i]==0):
            count+=1  
            i+=2 
        else:
            i-=1
            count+=1
            i+=2   
              
        
    if((c[len(c)-3]==1) or (len(c)==2) ):
        return count+1
    return count        
   




print(jumpingOnClouds(c))