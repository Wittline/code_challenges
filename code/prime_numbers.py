def prime_numbers_range(low, high):
    primes = []
    for num in range(low, high +1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)

    return primes


def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


