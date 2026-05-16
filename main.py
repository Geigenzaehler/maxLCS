import math
from lcs.exhaust import *;
from lcs.count import *;
from lcs.enumerateLCS import *;

s1 = 'aabbbaaabbbaaabbbaa'
s2 = 'bababababababababab'
enumerateLCS(s2, s1)

for i in range(2, 23):
    a = allstr_o(i,2)
    bw = "ba"*math.floor(i/2)
    if i%2 == 1:
        bw = bw + "b"
    b = [bw]
    print(maxD(a, b))
