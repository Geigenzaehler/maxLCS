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

