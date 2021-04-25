
s="hello world"
def solve(s):
    st= s.split(' ')
    stt=[]
    for i in st:
        stt.append(i.capitalize())
        
    s = ' '.join(stt)    
    print(s)  

solve(s) 
