import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    m =len(s)
    a_cnt = 0
    if(len(s)==1 and ('a' in s)):
        return n
    else:
        a_cnt = s.count('a')
        a_cnt = a_cnt * (n//m)
        k = n % m 
        a_cnt+=s[:k].count('a')
        
    return (a_cnt)

if __name__ == '__main__':
   
    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)