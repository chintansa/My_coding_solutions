s= [1,2,3]
s= [str(i) for i in s]

n = int(''.join(s))
n+=1
d = [int(i) for i in str(n)]
print(d)