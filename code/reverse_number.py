def reverse_number(n):
    
    nn = 0

    while n > 0:
        rem = n % 10
        nn = (nn * 10) + rem
        n = n // 10
    return nn

