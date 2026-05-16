import string;
from lcs.count import countLCS;

def allstr(n,k):
    C = string.ascii_lowercase[:k]
    r = [""]
    nr = []
    for i in range(n):
        for c in C:
            for s in r:
                nr.append(c+s)
        r = nr
        nr = []
    return r

def allstr2(n,k): # all strings of length n with exactly k distinct letters
    C = string.ascii_lowercase[:k]
    r = [""]
    nr = []
    for i in range(n):
        for c in C:
            for s in r:
                if c not in s:
                    nr.append(c+s)
        r = nr
        nr = []
    return r

def allstr_o(n,k): #all strings of length n with at most k distinct letters, and the first occurrence of the letters is in order
    letters = string.ascii_lowercase[:k]
    result = []

    def backtrack(pos, used_max, current):
        if pos == n:
            result.append("".join(current))
            return

        for i in range(min(used_max + 2, k)):
            current.append(letters[i])
            backtrack(pos + 1, max(used_max, i), current)
            current.pop()

    backtrack(0, -1, [])
    return result

def allstr_o2(n,k): #all strings of length n with exactly k distinct letters, and the first occurrence of the letters is in order
    letters = string.ascii_lowercase[:k]
    result = []

    def backtrack(pos, used_max, current):
        if pos == n:
            if used_max == k - 1:
                result.append("".join(current))
            return

        for i in range(min(used_max + 2, k)):
            current.append(letters[i])
            backtrack(pos + 1, max(used_max, i), current)
            current.pop()

    backtrack(0, -1, [])
    return result


def maxD(S):
    l = len(S)
    max = 0
    for i in range(l):
        for j in range(l):
            if countLCS(S[i], S[j]) > max:
                max = countLCS(S[i], S[j])
                print("New champion: " + str(max) + " " + S[i] + ", " + S[j])
            elif countLCS(S[i], S[j]) == max:
                print("Tied champion:" + str(max) + " " + S[i] + ", " + S[j])
    print("finish")
    return 1
    
def maxD(S, S2):
    l = len(S)
    l2 = len(S2)
    max = 0
    c1 = ""
    c2 = ""
    clist = []
    for i in range(l):
        for j in range(l2):
            if countLCS(S[i], S2[j]) > max:
                c1 = S[i]
                c2 = S2[j]
                max = countLCS(S[i], S2[j])
                #print("New champion: " + str(max) + " " + S[i] + ", " + S2[j])
                clist = [[c1, c2]]
            elif countLCS(S[i], S2[j]) == max:
                #print("Tied champion:" + str(max) + " " + S[i] + ", " + S2[j])
                clist.append([S[i], S2[j]])
    #print("finish")
    return max, c1, c2, clist

def D(t):
    m = t//2
    maxi = 0
    champ1 = ""
    champ2 = ""
    for l in range(1,m+1):
        So = allstr_o(t-l, l)
        S = allstr(l, l)
        max, c1, c2 = maxD(So, S)
        if(max > maxi):
            maxi = max
            champ1 = c1
            champ2 = c2
    return maxi, champ1, champ2
