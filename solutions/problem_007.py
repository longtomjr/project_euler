#!/usr/bin/env python3
import math


def prime_range(n: int) -> list:
    """
    Gets a range that the nth prime can reasonably be expected to be in
    Found the formula (from the Prime Number Theorem) here:
    https://math.stackexchange.com/questions/1257/is-there-a-known-mathematical-equation-to-find-the-nth-prime

    :param n: The index for a prime number
    :returns: A list with the lower an upper limit that the nth prime
              number can be expected to be in
    """

    # Note: math.log() returns the natural log if no base is specified
    range_min = n * math.log(n) + n * (math.log(math.log(n)) - 1)
    range_max = n * math.log(n) + n * math.log(math.log(n))
    return [math.ceil(range_min), math.ceil(range_max)]


def sieve_eratosthenes(n: int) -> list:
    """
    Finds all the Primes using the upper limit 'n' using
    Eratosthenes's Sieve algorithm
    More here: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode

    :param n: The upper limit of numbers to be tested for bieng primes
    :returns: list containing all the primes less than n
    """
    A = [True] * n
    primes = []
    for i in range(2, math.ceil(math.sqrt(n))):
        if A[i] is True:
            for j in range(i**2, n, i):
                A[j] = False

    for i in range(len(A)):
        if A[i] is True:
            primes.append(i)
    return (primes)


def P(n: int) -> list:
    """
    Gets the n-th prime number

    :param n: The index of the prime number
    :returns: The n-th prime number

    """
    return sieve_eratosthenes(prime_range(n)[1])[n + 1]


def main():
    print(P(10001))


if __name__ == "__main__":
    main()
