#Lexicographic sorting: Given a set of strings, return them in lexicographic order 

def lexicographicBubbleSort(words):
    swap = False

    for i in range(len(words)-1):
        for j in range(0, len(words)-i-1):            
            if words[j] > words[j+1]:
                words[j], words[j+1] = words[j+1], words[j]
                swap = True
        if not swap:
            return


words = [
    'lexicographic', 'sorting', 'of', 'a', 'set', 'of', 'keys', 'can', 'be',
    'accomplished', 'with', 'a', 'simple', 'trie', 'based', 'algorithm',
    'we', 'insert', 'all', 'keys', 'in', 'a', 'trie', 'output', 'all',
    'keys', 'in', 'the', 'trie', 'by', 'means', 'of', 'preorder',
    'traversal', 'which', 'results', 'in', 'output', 'that', 'is', 'in',
    'lexicographically', 'increasing', 'order', 'preorder', 'traversal',
    'is', 'a', 'kind', 'of', 'depth', 'first', 'traversal'
]
 
lexicographicBubbleSort(words)
 
print("Sorted array is:")
for i in range(len(words)):
    print(words[i], end=" ")        




