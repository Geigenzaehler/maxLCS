import math
from itertools import product

import numpy as np

from .count import countLCS
from .exhaust import allstr, allstr_o, maxD
from .upperboundDP import *


def gcdex(a, b):
    old_r, r = abs(a), abs(b)
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_s * (1 if a >= 0 else -1), old_t * (1 if b >= 0 else -1), old_r

def upperBoundDP(m,n): # For two strings of length m and n an upper bound of the number of longest common subsequences is D(m,n) = D(m-1,n-k) + D(m-2, n-k+2) + ... + D(m-k, n-1) where k is the k that maximises the sum. D(0,n) = D(m,0) = 1 for all m,n >= 0.
    D = [[0 for j in range(n+1)] for i in range(m+1)]
    K = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        D[i][0] = 1
    for j in range(n+1):
        D[0][j] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            k = 1
            kmax = min(i,j)
            k_applied = 0
            smax = 0
            s = 0
            while k <= kmax:
                for l in range(k):
                    s = s + D[i-l-1][j-k+l]  
                if s > smax:
                    smax = s
                    k_applied = k
                s = 0
                k += 1
            K[i][j] = k_applied
            D[i][j] = smax
    return D,K

def betcon(p1, p2, m1, m2, s1, s2, k): #p1, p2 are the prefixes, s1, s2 are the suffixes, k is the number of repetitions of the middle part
    c1 = len(p1 + s1)
    c2 = len(p2 + s2)
    e1 = len(m1)
    e2 = len(m2)
    #we now want to find i, j, such that c1+i*e1 = c2 + j*e2
    #using euklids extended algorithm
    x, y, g = gcdex(e1, e2)
    l = e1*e2//g
    m = e1*x*c2//g+e2*y*c1//g
    while m < 0:
        m = (m+l)%l
    if (c2-c1)%g != 0:
        print("no solution")
        return 0
    list = []
    for o in range(1,k):
        le = m+o*l
        i = (le-c1)//e1
        j = (le-c2)//e2
        A = p1 + m1*i + s1
        B = p2 + m2*j + s2
        t = len(A+B)
        count = countLCS(A,B)
        list.append([t,count])
        #print(A,B)
    #extraction of exponential growth rate
    

    data = np.array(list)
    data = np.array(data, dtype=float)
    x = data[:,0]
    y = data[:,1]

    # fit log(y) = m*x + b
    m, b = np.polyfit(x, np.log(y), 1)

    growth_rate = np.exp(m)
    C = np.exp(b)

    #print("a =", growth_rate)
    #print("C =", C)
    return growth_rate, C

def randomString(n, alphabet):
    import random
    s = ""
    for i in range(n):
        s = s + random.choice(alphabet)
    return s

def countMeanLCS(n, alphabet, trials):
    import math
    count = 0
    for i in range(trials):
        s1 = randomString(n, alphabet)
        s2 = randomString(n, alphabet)
        s = countLCS(s1,s2)
        count = count + math.log(s)
        
    return count/trials

def plotMeanLCS(n, alphabet, trials): 
    import matplotlib.pyplot as plt
    import math
    x = []
    y = []
    for i in range(1,n+1):
        x.append(i)
        y.append(countMeanLCS(i, alphabet, trials))
    
    plt.plot(x, y)
    
    plt.xlabel("n")
    
    plt.ylabel("mean(log LCS count)")
    plt.show()

def plotMeanLCSdiff(n, alphabet, trials):
    import matplotlib.pyplot as plt
    import math
    x = []
    y = []
    for i in range(2,n+1):
        x.append(i)
        y.append(countMeanLCS(i, alphabet, trials)-countMeanLCS(i-1, alphabet, trials))
    
    plt.plot(x, y)
    
    plt.xlabel("n")
    
    plt.ylabel("difference in mean(log LCS count)")
    plt.show()

def plotCountHistogram(n, alphabet, trials, log=True):
    import matplotlib.pyplot as plt
    import math
    x = []
    for i in range(trials):
        s1 = randomString(n, alphabet)
        s2 = randomString(n, alphabet)
        x.append(countLCS(s1,s2))
    if log:
        plt.hist([math.log(i) for i in x], bins=20)
    else:
        plt.hist(x, bins=30)
    plt.xlabel("LCS count")
    if log:
        plt.ylabel("log(count)")
    else:
        plt.ylabel("count")
    plt.show()

def multinomialCoefficient(n, k, b):
    if k < 0 or k > n*b:
        return 0
    if n == 0 and k == 0:
        return 1 
    L = np.ones(b+1, dtype=int)
    if n == 1:
        return L[k]
    for i in range(2, n+1):
        L1 = np.zeros(b*i+1, dtype=int)
        for j in range(len(L1)):
            for o in range(j-b, j+1):
                if o >= 0 and o < len(L):
                    L1[j] = L1[j] + L[o]
        L = L1
    return L[k]

def bestbinpred(k):
    return multinomialCoefficient(2*k, 2*k-1, 2) + 2*multinomialCoefficient(2*k-1, 2*k, 2) + multinomialCoefficient(2*k-2, 2*k+1, 2)

def binbestgraph():
    for k in range(1, 10):
        s1 = 'bbbaaa'*k
        s2 = 'ab'*(3*k)
        print(bestbinpred(k))
        print(countLCS(s1, s2))  

    D, K = tighterUpperBoundDP(20,20)
    for i in range(20):
        print(K[i])

    import matplotlib.pyplot as plt

    ns = list(range(4, 201, 2))   # n values
    vals = []

    alphabet = "ab"
    trials = 200

    for n in ns:
        v = countMeanLCS(n, alphabet, trials)
        vals.append(v)
        print(n, v)

    plt.plot(ns, vals, marker='o')
    plt.xlabel("n")
    plt.ylabel("mean(log(#LCS))")
    plt.title("Growth of average logged LCS count")
    plt.grid(True)

    plt.show()
    return 0

def applyDP(n, X, Y, LX, LY): # 
    L = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(1,n+1):
        L[i][0] = L[i-1][0]+LX[i-1]
    for j in range(1,n+1):
        L[0][j] = L[0][j-1]+LY[j-1]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    D = [[[0,0] for j in range(n+1)] for i in range(n+1)]
    for i in range(n+1):
        D[i][n-i][1] = 1
    for i in range(1,n+1):
        D[i][n+1-i][0] = 1
    for s in range(n+2,2*n+1):
        for i in range(s-n, n+1):
            j = s-i
            if X[i-1] == Y[j-1]:
                D[i][j][0] = D[i-1][j-1][0]
                D[i][j][1] = D[i-1][j-1][1]
            else:
                if L[i-1][j] > L[i][j-1]:
                    D[i][j][0] = D[i-1][j][0]
                    D[i][j][1] = D[i-1][j][1]
                if L[i-1][j] < L[i][j-1]:
                    D[i][j][0] = D[i][j-1][0]
                    D[i][j][1] = D[i][j-1][1]
                if L[i-1][j] == L[i][j-1] and L[i-1][j] != L[i][j]:
                    D[i][j][0] = D[i-1][j][0]+D[i][j-1][0]
                    D[i][j][1] = D[i-1][j][1]+D[i][j-1][1]
                if L[i-1][j] == L[i][j-1] and L[i-1][j] == L[i][j]:
                    D[i][j][0] = D[i-1][j][0]+D[i][j-1][0]-D[i-1][j-1][0]
                    D[i][j][1] = D[i-1][j][1]+D[i][j-1][1]-D[i-1][j-1][1]
    return D[n][n];

def DPub(n):
    max = 0
    arrays = list(product([0, 1], repeat=n))
    for X in allstr(n, 2):
        for Y in allstr(n, 2):
            for LX in arrays:
                for LY in arrays:
                    if applyDP(n, X, Y, LX, LY)[0] + applyDP(n, X, Y, LX, LY)[1] > max:
                        max = applyDP(n, X, Y, LX, LY)[0] + applyDP(n, X, Y, LX, LY)[1]
                        print(X, Y, LX, LY, applyDP(n, X, Y, LX, LY))

def DBin(t):
    m = t//2
    maxi = 0
    champ1 = ""
    champ2 = ""
    for l in range(1,m+1):
        So = allstr_o(t-l, 2)
        S = allstr(l, 2)
        max, c1, c2, clist = maxD(So, S)
        if(max > maxi):
            maxi = max
            champ1 = c1
            champ2 = c2
    return maxi, champ1, champ2

def binmaxSearch(n):
    l = []
    for i in range(1, n+1):
        l = l + allstr(i, 2)
    
    for m1 in l:
        for m2 in ["ab"]:
            g, c = betcon("", "", m1, m2, "", "", 12)
            if g > 1.19:
                print(m1, m2, g, c)

def E(n, estimate=False):
    if estimate:
        count = 0
        trials = 10000
        for i in range(trials):
            s1 = randomString(n, "ab")
            s2 = randomString(n, "ab")
            s = countLCS(s1,s2)
            count = count + math.log(s)
            
        return count/trials
    X = allstr(n, 2)
    Y = allstr(n, 2)
    count = 0
    for x in X:
        for y in Y:
            count = count + math.log(countLCS(x,y))

    return count/(len(X)*len(Y))

def surdiff(n, estimate=False):
    
    l = []
    if estimate:
        trials = 100
        for i in range(trials):
            m1 = randomString(n, "ab")
            m2 = randomString(n, "ab")
            o = countLCS(m1, m2)
            o1 = countLCS("a"+m1+"a", "b"+m2+"b")
            o2 = countLCS("b"+m1+"b", "a"+m2+"a")
            o3 = countLCS("a"+m1+"b", "b"+m2+"a")
            o4 = countLCS("b"+m1+"a", "a"+m2+"b")
            l.append(o1-o)
            l.append(o2-o)
            l.append(o3-o)
            l.append(o4-o)
    else:
        X = allstr(n, 2)
        for m1 in X:
            for m2 in X:
                o = countLCS(m1, m2)
                o1 = countLCS("a"+m1+"a", "b"+m2+"b")
                o2 = countLCS("b"+m1+"b", "a"+m2+"a")
                o3 = countLCS("a"+m1+"b", "b"+m2+"a")
                o4 = countLCS("b"+m1+"a", "a"+m2+"b")
                l.append(o1-o)
                l.append(o2-o)
                l.append(o3-o)
                l.append(o4-o)
    # histogram of l
    import matplotlib.pyplot as plt
    import numpy as np
    plt.hist(l, bins=np.arange(min(l), max(l) + 1) - 0.5, density=True)
    plt.xlabel("Difference in LCS count")
    plt.ylabel("Density")
    plt.title("Distribution of LCS count differences")
    plt.grid(True)
    plt.show()


                    
