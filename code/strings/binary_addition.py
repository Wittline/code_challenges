def add_binary(a, b):

    res = ''
    carry = 0
    
    max_len = max(len(a), len(b))
    
    a = '0' * (max_len - len(a)) + a
    b = '0' * (max_len - len(b)) + b

    for i in range(max_len -1 , -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0

        res  = ('1' if r % 2 == 1 else '0') + res

        carry = 0 if r < 2 else 1
    
    if carry > 0:
        res = '1' + res
    
    return res




    