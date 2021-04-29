n = 6

c = 2

m = 2

def chocolateFeast(n, c, m):
    wrappers = n//c
    plusChoco= wrappers
    while(wrappers>=m):
        remain = wrappers % m
        wrappers //= m
        plusChoco+=wrappers
        wrappers+=remain

    return plusChoco



print(chocolateFeast(n, c, m))    