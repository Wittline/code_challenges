
from re import M


def binary_search(words, low, high, word):

    if high >= low:

        m = (high + low) // 2

        if words[m] == word:
            return m
        elif words[m] > word:
            return binary_search(words, low, m -1, word)
        else:
            return binary_search(words, m+1, high, word)
    else:
        return -1



words = [
    'lexicographic', 'sorting', 'of', 'a', 'set', 'of', 'keys', 'can', 'be',
    'accomplished', 'with', 'a', 'simple', 'trie', 'based', 'algorithm',
    'we', 'insert', 'all', 'keys', 'in', 'a', 'trie', 'output', 'all',
    'keys', 'in', 'the', 'trie', 'by', 'means', 'of', 'preorder',
    'traversal', 'which', 'results', 'in', 'output', 'that', 'is', 'in',
    'lexicographically', 'increasing', 'order', 'preorder', 'traversal',
    'is', 'a', 'kind', 'of', 'depth', 'first', 'traversal'
]

word = 'means'

words.sort()
 

result = binary_search(words, 0, len(words)-1, word)
 
if result != -1:
    print("Word is present in words at index", str(result))
else:
    print("Word is not present in words")