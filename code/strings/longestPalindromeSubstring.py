def longestPalindromeSubstring(s):

    def explore(l, r):
        while (l>=0 and r<len(s) and s[l] == s[r]):
            l -=1
            r +=1
        return s[l+1:r]

    result = ''
    for i in range(1, len(s)):
        sub1 = explore(i, i)
        result = sub1 if len(sub1)> len(result) else result
        sub2 = explore(i, i+1)
        result = sub2 if len(sub2)> len(result) else result
    return result