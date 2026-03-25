def FirstLCS(x, y, i1, i2, j1, j2):
    if i1 == i2:
        for j in range(j1, j2+1):
            if x[i1] == y[j]:
                return [j]
        return []
    #-----------------------------------------
    Jneg = []        
    Jpos = []
    icut = (i1+i2)//2
    for i in range(i1, icut+1):
        p = len(Jneg)
        for j in range(j2, j1-1, -1):
            if p>0 and Jneg[p-1] == j:
                p = p-1
            if x[i] == y[j]:
                if len(Jneg) == p:
                    Jneg = Jneg+[j]
                else:
                    Jneg[p] = j
    #-----------------------------------------
    for i in range(i2, icut, -1):
        q = len(Jpos)
        for j in range(j1, j2+1):
            if q>0 and Jpos[q-1] == j:
                q = q-1
            if x[i] == y[j]:
                if len(Jpos) == q:
                    Jpos = Jpos+[j]
                else:
                    Jpos[q] = j
    #-------------------------------------------
    p = 0
    q = len(Jpos)
    r = p+q
    jcut = j1-1
    for j in range(j1, j2+1):
        if len(Jneg)>p and Jneg[p]<=j:
            p = p+1
        if q>0 and Jpos[q-1]<=j:
            q = q-1
        if p+q>r:
            jcut = j
            r = p+q

    return FirstLCS(x, y, i1, icut, j1, jcut)+FirstLCS(x, y, icut+1, i2, jcut+1 , j2)

def findBranch(x,y,P):
    Q = []
    k = 0
    for i in range(0, len(x)):
        if k<len(P) and x[i] == y[P[k]]:
            Q = Q + [i]
            k = k+1
    #-----------------------------------------
    istar = len(x)-1
    J = []
    for k in range(len(P)-1, -1, -1):
        while(istar >= Q[k]):
            J, istar = decI(x, y, J, istar)
        for j in range(P[k]+1, len(y)):
            if(k == 0):
                i = -1
            else:
                i = Q[k-1]
            i = i+1
            while not(istar + 1 == i or x[i] == y[j]):
                i = i+1
            if i<=istar:
                while(istar >= i+1):
                    J, istar = decI(x, y, J, istar)
                if len(J) >= len(P)-k-1 and (j+1 <= J[len(P)-k-2] or len(P)-k-2 == -1):
                    return k, i, j
                else:
                    J, istar = decI(x, y, J, istar)
    return "end", 0, 0
        
def decI(x, y, J, i):
    i = i-1;
    l = len(J)-1
    for j in range(0, len(y)):
        if l>=0 and J[l] == j:
            l = l-1
        if x[i+1] == y[j]:
            if len(J) == l+1:
                J = J+[j]
            else:
                J[l+1] = j
    return J, i

def enumerateLCS(x, y):
    P = []
    k = 0
    c = 0
    istart = 0
    jstart = 0
    while(k != "end"):
        P = P[0:k]+FirstLCS(x, y, istart, len(x)-1, jstart, len(y)-1)
        print(P, ''.join([y[i] for i in P]))
        k, istart, jstart = findBranch(x, y, P)
        c = c+1
    return c
