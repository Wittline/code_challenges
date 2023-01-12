#check if string is palindrome
def is_palindrome(s):

    ns = ''.join(c for c in  s if c != ' ')
    
    return ns == ns[::-1]



print(is_palindrome('lev el isi level'))