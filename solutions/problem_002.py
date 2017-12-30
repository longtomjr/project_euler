#! usr/bin/env python3


def F(n: int) -> int:
    """
    Function that is a python version of the mathematical
    function
          {0 -            if n = 0;
    F_n = {1 -            if n = 1;
          {F_n-1 + F_n-2  if n > 1.

    :param n: The term of the sequance you want
    :returns: The n-th term of the fibonacci sequance
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n - 1) + F(n - 2)


def fib(n: int) -> list:
    """
    Generates a 'list' of the fibonacci sequance to the nth term

    :param n: the length of the sequance
    :returns: A list with the fibonacci sequence
    """
    sequence = []
    for i in range(n + 1):
        sequence.append(F(i))
    return sequence


def fibonacci_max_n(maximum: int) -> int:
    """
    Gets 'n' of the largest fibonacci number less than the max

    :param maximum: The number that may not be exeeded
    :returns: 'n' of the largest number less than the max
    """

    n = 0
    # Infinite loop that will continue until broken
    while True:
        # Makes 'n' larger until the fibonacci number is to large
        if F(n) < maximum:
            n = n + 1
            continue
        else:
            # Return will break the loop
            # This 'else' clause will only be reached once n is one to large
            # therefore I can get the correct value of n by just subtracting 1
            return n-1


def sum_of_even_terms(l: list) -> int:
    """
    Gets the sum of all the even terms in a list

    :param l: The list to be used to get the sums
    :returns: The sum of all the even terms in 'l'
    """
    s = 0
    for i in l:
        # If a number is even, it will be a factor of 2
        # therefore it will be cleanly divisible by 2
        if i % 2 == 0:
            s = s + i
        else:
            continue
    return s


def main():
    # Order of events:
    # 1. Get max n
    # 2. Get the sequence to n
    # 3. Gets the sum of all the even terms
    # 4. Prints the result
    print(sum_of_even_terms(fib(fibonacci_max_n(4000000))))


"""
Footnotes:
 - The code can be made a lot more efficient if you only have to get the
   sequence once. (currently we get it with max_n, and fib)
   - This is however was not a priority for me since it is easier to see
     How it works this way. If you want to you can try and code a more
     efficient example eliminating the 2nd sequence contstructing

 - A way better implementaion would be using https://i.stack.imgur.com/SPYOU.gif
   Since it is super fast to compute and way more efficient
   - Chalenge: Try to rewrite this script using this equation

     - Hint 1: Use the 'math' library "import math"

     - If you are stuck go read this Stack Overflow Q and A
       https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python

"""

if __name__ == "__main__":
    main()
