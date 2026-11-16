import math
from lcs.exhaust import *;
from lcs.count import *;    
from lcs.enumerateLCS import *;
from lcs.upperboundDP import *;

s1 = 'bbbaaabbbaaabbbaaa'
s2 = 'bababababababababa'

print(countLCS(s1,s2))

print(countLCS("abcd"*9,"dcba"*9))
print(D_ub(72))

for i in range(0,13):
    print(D(i))

    