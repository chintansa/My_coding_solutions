N = 1000000000
cells=[1,0,0,1,0,0,1,0]

cell_len =len(cells)
cells_new=[]

if(N>14):
    N= 14+(N%14)

for _ in range(N):
    cells_new.append(0)
    for i in range(1,cell_len-1):
        if((cells[i-1]+cells[i+1])%2==0):
            cells_new.append(1)
        else:
            cells_new.append(0)

    cells_new.append(0)
    cells=cells_new
    cells_new=[]  
  

print(cells)