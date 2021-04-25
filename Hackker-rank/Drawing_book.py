n = int(input().strip())            #the number of pages in the book
p = int(input().strip())            #the page number to turn to

# def pageCount(n, p):
# Write your code here

#convert to the nearest even int
if(n%2!=0):
    n = n-1
if(p%2!=0):
    p= p-1

#check from 1st page
n_th = int(abs((p/2)-(n/2)))

if(n_th <= (p//2)):
    print(n_th)
else:
    print(p//2)    



