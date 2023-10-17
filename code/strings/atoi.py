def atoi(s):
    s = s.strip()
    if not s:
        return 0
    
    sign = 1
    if s[0] in "+-":
        sign = -1 if s[0] == "-" else 1
        s = s[1:]
    
    num = 0
    for char in s:
        if not char.isdigit():
            break
        num = num * 10 + int(char)
    
    num = min(max(sign * num, -2**31), 2**31 - 1)
    return num