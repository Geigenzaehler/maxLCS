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
