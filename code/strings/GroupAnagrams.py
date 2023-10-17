def groupAnagrams(strs):

    if len(strs)< 1:
        return [strs]
        
    groups = {}
    for word in strs:
        mword = ''.join(sorted(word))
        

        if mword in groups:
            groups[mword].append(word)
        else:
            groups[mword] = []
            groups[mword].append(word)        

    return [v for v in groups.values()]