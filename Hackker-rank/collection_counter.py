# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

from collections import Counter
t_len=input()
l=list(map(int,(input()).split(' ')))
vv = Counter(l)
sum=0
num_shoes = int(input())

for _ in range(num_shoes):
    i =list(map(int,input().split()))
    if(vv[i[0]]>0):
        sum+=i[1]
        vv[i[0]]-=1
    else:
        pass

print(sum)
