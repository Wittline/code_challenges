from cgitb import small


def HCF(n1, n2):
    
    smaller = min (n1, n2)
    for i in range(1, smaller + 1):
        if n1 % i == 0 and n2 % i == 0:
            factor = i
    return factor


