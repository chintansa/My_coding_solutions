s="abcabcbb"
n = len(s)
sub_temp=''
for i in range(n):
    for j in range(i,n):
        sub_s = s[i:j]
        if(len(sub_s)==len(set(sub_s))):
            if(len(sub_s)>len(sub_temp)):
                sub_temp= sub_s

print(len(sub_temp))      