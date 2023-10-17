def lengthOfLongestSubstring(s):        
    ml, l, r = 0, 0, 0
    seen = {}

    while r < len(s):
        
        if s[r] in seen:
            l  = max(l, seen[s[r]] + 1)

        seen[s[r]] = r
        ml = max(ml, r - l + 1)        

        r += 1
    
    return ml