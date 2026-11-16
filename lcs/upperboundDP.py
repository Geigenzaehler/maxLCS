def upperBoundDPTable(m,n): 
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

def D_ub3(m,n,l):
    D, K = upperBoundDPTable(m,n)
    return D[l][m][n]

def D_ub2(m,n):
    D, K = upperBoundDPTable(m,n)
    return K[m][n]

def D_ub(t):
    D, K = upperBoundDPTable(t,t)
    max = 0
    for i in range(0, t+1):
        j = t-i
        if K[i][j] > max:
            max = K[i][j]
    return max

