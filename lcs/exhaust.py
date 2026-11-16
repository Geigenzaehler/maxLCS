import string;
from .count import countLCS

def allstr(n,k): # all strings of length n with at most k distinct letters
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

    
def maxD(S, S2): # returns the maximum number of LCS between two sets of strings S and S2, along with the pair of strings that achieve this maximum and a list of all pairs that achieve this maximum
    max_val = 0
    c1 = ""
    c2 = ""
    clist = []

    for s in S:
        for s2 in S2:
            count = countLCS(s, s2)

            if count > max_val:
                c1, c2 = s, s2
                max_val = count
                clist = [[s, s2]]
            elif count == max_val:
                clist.append([s, s2])

    return max_val, c1, c2, clist

def D(t): # returns the maximum number of LCS between two strings of length t, along with the pair of strings that achieve this maximum
    if(t==0):
        return 1, "", ""
    if(t==1):
        return 1, "a", ""
    m = t//2
    maxi = 0
    champ1 = ""
    champ2 = ""
    for l in range(1,m+1):
        So = allstr_o(t-l, l)
        S = allstr(l, l)
        max, c1, c2, clist = maxD(So, S)
        if(max > maxi):
            maxi = max
            champ1 = c1
            champ2 = c2
    return maxi, champ1, champ2





