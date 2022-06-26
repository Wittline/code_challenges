def LCSubStr(str1, str2, N, M):
 
    LCSuff = [[0 for k in range(M+1)] for l in range(N+1)]
    mx = 0
    for i in range(N + 1):
        for j in range(M + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (str1[i-1] == str2[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                mx = max(mx, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return mx

def lcs(i, j, count):
 
    if (i == 0 or j == 0):
        return count
 
    if (str1[i - 1] == str2[j - 1]):
        count = lcs(i - 1, j - 1, count + 1)
 
    count = max(count, max(lcs(i, j - 1, 0),
                           lcs(i - 1, j, 0)))
 
    return count    

str1 = "holalala"
str2 = "lalalaw"

print(lcs(len(str1), len(str2), 0))