
def binary_search_word(words, low, high, word):

    if high >= low:

        m = (high + low) // 2

        if words[m] == word:
            return m
        elif words[m] > word:
            return binary_search_word(words, low, m -1, word)
        else:
            return binary_search_word(words, m+1, high, word)
    else:
        return -1


def binary_search_max_word_unsorted(words, low, high):
    max = 0
    if low == high:
        max = words[low]
    elif low + 1 == high:
        if words[low] < words[high]:
            max = words[high]
        else:
            max = words[low]
    else:
        mid = low + (high - low) // 2
        lmax = binary_search_max_word_unsorted(words, low, mid)
        hmax = binary_search_max_word_unsorted(words, mid + 1, high)
        if lmax > hmax:
            max = lmax
        else:
            max = hmax

    return max



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
 
result = binary_search_max_word_unsorted(words, 0, len(words)-1)

if result != -1:
    print("Max Word is:", str(result))
else:
    print("Word is not present in words") 


words.sort()

result = binary_search_word(words, 0, len(words)-1, word)
 
if result != -1:
    print("Word is present in words at index", str(result))
else:
    print("Word is not present in words")


