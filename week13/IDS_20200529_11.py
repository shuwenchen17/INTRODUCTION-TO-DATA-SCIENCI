def is_prime(x):
    """
    Returns True if x is a prime, or returns False
    """
    divisors = []
    for i in range(1, x+1):
        if x % i == 0:
            divisors.append(i)
    n_divisors = len(divisors)  
    return n_divisors == 2
   
print(is_prime(6))    