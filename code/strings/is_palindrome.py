def is_palindrome(s):

    alnum = [c.lower() for c in s if c.isalnum()]
    return alnum == alnum[::-1]