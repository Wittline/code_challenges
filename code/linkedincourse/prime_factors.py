#find prime factors

def find_prime_factors(n):
    
    divisor = 2 
    factors = []

    while divisor <= n:

        if n % divisor == 0:
            factors.append(divisor)
            n = n//divisor            
        else:
            divisor += 1
    
    return factors



print(find_prime_factors(60))



