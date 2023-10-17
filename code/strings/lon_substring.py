
def longestUniqueSubsttr(s):
      

    seen = {}
    maximum_length = 0
  

    start = 0
      
    for end in range(len(s)):
  
        if s[end] in seen:
 
            start = max(start, seen[s[end]] + 1)
  
        seen[s[end]] = end
        maximum_length = max(maximum_length, end-start + 1)
    return maximum_length