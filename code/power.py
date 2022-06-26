def power2(x, n):
    aux = 0
    result = x
    while aux < n-1:

        result = x * result
        aux += 1

    return result

def power(x, n):

    if n == 0:
        return 1

    p = power(x, n // 2)

    if n % 2:
        return x * p * p
    
    return p * p

def pow(x, n):
    if n >= 0:
        return power2(x, n)
    else:
        return 1/power2(x, -1*n)

pows = [(4,2), (5,4), (3,2), (2,-2), (5,-3)]


for p in pows:
    print(p[0], p[1], pow(p[0], p[1]))




