import math
def countLCS(x,y):
    L = [[0 for j in range(len(y)+1)] for i in range(len(x)+1)]
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            if x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    B = [[0 for j in range(len(y))] for i in range(len(x))]
    fi = 0
    fj = 0
    for i in range(len(x)):
        if x[i] == y[0] or fi == 1:
            B[i][0] = 1
            fi = 1
    for j in range(len(y)):
        if y[j] == x[0] or fj == 1:
            B[0][j] = 1
            fj = 1
    for i in range(1,len(x)): 
        for j in range(1,len(y)):
            if x[i] == y[j]:
                if B[i-1][j-1] == 0:
                    B[i][j] = 1
                else:
                    B[i][j] = B[i-1][j-1]
            else:
                if L[i+1][j] > L[i][j+1]:
                    B[i][j] = B[i][j-1]
                if L[i+1][j] < L[i][j+1]:
                    B[i][j] = B[i-1][j]
                if L[i+1][j] == L[i][j+1] and L[i+1][j] != L[i][j]:
                    B[i][j] = B[i][j-1]+B[i-1][j]
                if L[i+1][j] == L[i][j+1] and L[i+1][j] == L[i][j]:
                    B[i][j] = B[i][j-1]+B[i-1][j]-B[i-1][j-1]
    #for i in L:
    #    print(i)
    #for i in B:
    #    print(i)
    #R = []
    return B[len(x)-1][len(y)-1]

def dpLCS(x,y):
    L = [[0 for j in range(len(y)+1)] for i in range(len(x)+1)]
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            if x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    return L

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

def tighterUpperBoundDP(m,n): # For two strings of length m and n an upper bound of the number of longest common subsequences of length l is D(m,n,l) = D(m-1,n-k, l-1) + D(m-2, n-k+2, l-1) + ... + D(m-k, n-1, l-1) where k is the k that maximises the sum. D(0,n) = D(m,0) = 1 for all m,n >= 0.
    D = [[[0 for j in range(n+1)] for i in range(m+1)] for l in range(min(m,n)+1)]
    K = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            D[0][i][j] = 1
    for l in range(1, min(m,n)+1):
        for i in range(1,m+1):
            for j in range(1,n+1):
                k = 1
                kmax = min(i,j)
                
                smax = 0
                s = 0
                while k <= kmax:
                    for o in range(k):
                        s = s + D[l-1][i-o-1][j-k+o] 
                    if s > smax:
                        smax = s
                    s = 0
                    k += 1
                
                D[l][i][j] = smax
    for i in range(0,m+1):
            for j in range(0,n+1):
                for o in range(min(i,j)+1):
                    if D[o][i][j] > K[i][j]:
                        K[i][j] = D[o][i][j]
    return D,K

def betcon(p1, p2, s1, s2, k): #p1, p2 are the prefixes, s1, s2 are the suffixes, k is the number of repetitions of the middle part
    for i in range(1,k):
        A = p1 + "abcde"*i + s1
        B = p2 + "edcba"*i + s2
        t = len(A+B)
        count = countLCS(A,B)
        C = count * math.sqrt(t)/4**(t/5)*math.sqrt(math.pi)
        print(C)
    return 0

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
        count = count + countLCS(s1,s2)
    return count/trials, math.log(count/trials)/n

def plotMeanLCS(n, alphabet, trials, log=True):
    import matplotlib.pyplot as plt
    import math
    x = []
    y = []
    for i in range(1,n+1):
        x.append(i)
        y.append(countMeanLCS(i, alphabet, trials))
    if log:
        plt.plot(x, [math.log(i) for i in y])
    else:
        plt.plot(x, y)
    plt.xlabel("n")
    if log:
        plt.ylabel("log(mean LCS count)")
    else:
        plt.ylabel("mean LCS count")
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
        plt.hist(x, bins=20)
    plt.xlabel("LCS count")
    if log:
        plt.ylabel("log(count)")
    else:
        plt.ylabel("count")
    plt.show()