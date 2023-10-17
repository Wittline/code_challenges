#Find the Index of the First Occurrence in a String

def strStr(haystack, needle):

    # if len(haystack) < len(needle):
    #         return -1

    # r, page = 0, len(needle)

    # while r < len(haystack):

    #     if haystack[r:r+page] == needle:
    #         return r
    #     else:
    #         r +=1
            
    # return -1

    if len(haystack) < len(needle):
        return -1

    positions_first = []

    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            positions_first.append(i)
    
    for pos in positions_first:
        if haystack[pos:pos + len(needle)] == needle:
            return pos

    return -1




