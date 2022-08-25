def isSubsequence(word, s):    
    n = len(word)
    m = len(s)
    i = 0
    j = 0

    while j < m and i < n:
        if word[j] == s[i]:
            j = j + 1
        i = i + 1
    
    return j == m

words = []
s = ""
count = 0

def count_words_subsequence(words, s):

    for word in words:
        if isSubsequence(word, s):
            count += 1
    return count