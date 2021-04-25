n = 715950220  
m = 876882456
s = 195550680

m %= n
res = (m + s - 1) % n
if res == 0:
    res = n
print(res)