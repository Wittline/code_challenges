
# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(words):


    min_len = min([len(word) for word in words])
    result = ''

    for i in range(1, min_len + 1):
        prefix = words[0][:i]
        for word in words:
            if word[0:i] != prefix:
                return result
        result = prefix
    
    return result




