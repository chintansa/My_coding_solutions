n = list(map(int,input()))
n.append('a')
final =[]
j=0
i=0
count=1 
while(i+1<len(n)):    
    if(n[i] == n[i+1]):
        count+=1
        i+=1
    else:
        final.append((count,n[i]))
        i=i+1
        count =1

for i in final:           
    print(i)


