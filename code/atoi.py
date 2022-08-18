def atoi(s):
    rtr=0
    for c in s:
        rtr=rtr*10 + ord(c) - ord('0')

    return rtr