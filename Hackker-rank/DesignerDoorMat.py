
#loop for welcome
def welcome():
    rng=(m-7)//2
    for i in range(rng):
        print('-',end='')
    print('WELCOME',end='') 
    for i in range(rng):
        print('-',end='')
    print()    

#loop for forward print

def FirstPrint():
    limit=n//2
    j=m
    k=3
    for i in range(limit):
        for i in range((j-k)//2):
            print('-',end='')
        for i in range(k//3):
            print('.|.',end='') 
        for i in range((j-k)//2):
            print('-',end='')       
        k+=(3*2)
        print()
    return k

def SecondPrint(kk):
    limit=n//2
    j=m
    k= kk-(3*2)
    for i in range(limit):
        for i in range((j-k)//2):
            print('-',end='')
        for i in range(k//3):
            print('.|.',end='') 
        for i in range((j-k)//2):
            print('-',end='')       
        k-=(3*2)
        print()



if __name__ == "__main__":
    nm=list(map(int,input().split(' ')))
    n = nm[0]
    m = nm[1]
    kk=FirstPrint()
    welcome() 
    SecondPrint(kk)
    

