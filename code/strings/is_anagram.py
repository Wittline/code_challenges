def isAnagram(self, s, t):

    if len(s) != len(t):
        return False
    
    c_count = {}
    for c in s:
        c_count[c]= 1 + c_count.get(c, 0)

    for c in t:
        if c not in c_count:
            return False            
        c_count[c] -= 1
    

    for v in c_count.values():
        if v != 0:
            return False
    
    return True