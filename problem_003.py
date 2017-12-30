#! usr/bin/env python3

# This is an import statement. It is used to import modules with
# Numerous handy functions and types
# More on modules: https://docs.python.org/3/glossary.html#term-module
import math


def fermat_factors(N: int) -> tuple:
    """
    Gets the factors of a odd number 'N' using Fermat's factorization
    method.

    :param N: Odd number to be factorized
    :returns: A tuple containing the 2 Fermat factors
    """

    # Does a check to see if the input was odd
    if N % 2 == 0:
        # Raising/Trowing an exeption (error) to make sure nothing
        # happens that will break something bigger and make the error
        # Easily traceable
        raise SyntaxError("N should be odd")

    # When using functions from a module, always write as
    # 'module.function()' [Exept when using a 'for' import clause]
    a = math.ceil(math.sqrt(N))
    b2 = a**2 - N

    while math.sqrt(b2) % 1 != 0:
        a = a + 1
        b2 = a**2 - N

    # We are returning a tuple containing the 2 factors we got
    # Tuples are a colletion data type
    # more on tuples: https://docs.python.org/3/library/stdtypes.html#tuples
    # Tuples are stored like (1, 2)
    return (int(a - math.sqrt(b2)), int(a + math.sqrt(b2)))

def prime_factors(N: int) -> list:
    """
    Returns the prime factors of an odd number 'N'

    :param N: Odd number to be prime factorized
    :returns: List of all the prime factors of 'N'
    """
    factors = [fermat_factors(N)]
    primes = []
    for factor_pair in factors:
        # If the first factor is 1, we know we have a prime
        if factor_pair[0] == 1:
            primes.append(factor_pair[1])
        else:
            factors.append(fermat_factors(factor_pair[0]))
            factors.append(fermat_factors(factor_pair[1]))
    return primes





def main():
    primes = prime_factors(600851475143)
    print(primes)
    print(max(primes))


if __name__ == "__main__":
    main()
