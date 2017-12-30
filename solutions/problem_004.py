#!/usr/bin/env python3


def max_palindrome_product(max_number: int) ->int:
    """
    Gets the maximum product of two numbers less than the given
    maximum that is a palindrome

    :param max_number: The maximum value of the two numbers
    :returns: The largest palindromic number
    """
    palindromes = []
    for x in range(max_number, 1, -1):
        for y in range(max_number, 1, -1):
            if is_palindrome(str(x * y)):
                palindromes.append(x*y)
            else:
                continue
    return max(palindromes)


def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome

    :param s: String to be tested
    :returns: True if a palindrome, False if not
    """
    if s == s[::-1]:
        return True
    else:
        return False



def main():
    print(max_palindrome_product(999))
    return 0


if __name__ == "__main__":
    main()
