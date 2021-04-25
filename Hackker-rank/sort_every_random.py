s = 'Sorting1234' #input()
s = sorted(s)
small_l=[]
large_l=[]
num_l_even =[]
num_l_odd = []
for i in s:
    if(ord(i)>=97 and ord(i)<=122):
        small_l.append(i)
    elif(ord(i)>=65 and ord(i)<=90):
        large_l.append(i)
    else:
        if(int(i)%2==0):
            num_l_even.append(i)
        else:
            num_l_odd.append(i)    

print(''.join(small_l+large_l+num_l_odd+num_l_even) )       