n =  int(input())
r= input().split()
print(r)
rooms = list(map(int,r)).sort()
print(rooms)
r_set = list(set(rooms))

for i in r_set:
    if(rooms.count(i)<n):
        print(i)