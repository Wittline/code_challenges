def longestCommonSubsequence(self, m, n):        

    L = [[None]*(len(n)+1) for i in range(len(m)+1)]
    
    for i in range(len(m)+1):
        for j in range(len(n)+1):

            if i == 0 or j==0:
                L[i][j] = 0
            elif m[i-1] == n[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

        
    return L[len(m)][len(n)]