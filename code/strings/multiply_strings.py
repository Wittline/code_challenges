def multiply_strings(num1, num2):

    rtr1 = 0
    rtr2 = 0

    for n in num2:
        rtr1 = rtr1 * 10 + ord(n) - ord('0')

    for n in num1:
        rtr2 = rtr2 * 10 + ord(n) - ord('0')
    
    return str(rtr1 * rtr2)
