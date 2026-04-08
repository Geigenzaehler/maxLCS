import math
from lcs.exhaust import *;
from lcs.count import *;

def betcon(p1, p2, s1, s2, k): #p1, p2 are the prefixes, s1, s2 are the suffixes, k is the number of repetitions of the middle part
    for i in range(1,k):
        A = p1 + "abcde"*i + s1
        B = p2 + "edcba"*i + s2
        t = len(A+B)
        count = countLCS(A,B)
        C = count * math.sqrt(t)/4**(t/5)*math.sqrt(math.pi)
        print(C)
    return 0
#betcon("","","","",100)
v = 80
u,k = upperBoundDP(v,v)
#for i in range(v+1):
    #print(u[i])
    #print(k[i])
print(u[80][80])