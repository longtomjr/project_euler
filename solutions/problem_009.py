#!/usr/bin/env python3


def euclid_pyth_triplet(n, m):
    """
    Creates a pythagorean triplet using a variant of Euclid's formula
    More here:
    https://en.wikipedia.org/wiki/Pythagorean_triple#A_variant
    http://www.friesian.com/pythag.htm

    :param n: A odd integer to use for generating a triplet
    :param m: An odd integer larger than 'n' for generating a triplet
    :returns: List containing 3 integers that make up a pythagorean triplet
    """
    if n % 2 == 0 or m % 2 == 0:
        raise SyntaxError("n or m is even and should be odd")
    a = n * m
    b = (m**2 - n**2) / 2
    c = (m**2 + n**2) / 2
    return [int(a), int(b), int(c)]


def pyth_triplet_test(triplet):
    """
    Checks if a given list of 3 integers is a pythagorean triplet

    :param triplet: List of 3 integers to be tested
    :returns: 'True' if 'triplet' is a pythagorean triplet, 'False' if not
    """
    if triplet[0]**2 + triplet[1]**2 == triplet[2]**2:
        return True
    else:
        return False


def triplet_sum(l, target):
    """
    Checks if the sum of a given triplet is equal to the target sum

    :param l: List containing 3 integers
    :param target: The target sum
    :returns: 'True' if the sum of 'l' is equal to the target sum
    """
    if l[0] + l[1] + l[2] == target:
        return True

    else:
        return False


def find_triplet_with_sum(range_max, target_sum):
    """
    Creates several pythagorean triplets to find a triplet that adds up
    to the target sum

    :param range_max: The max range to be used to generate the triplets
    :param target_sum: The sum that wants to be achieved
    :returns: A list with 3 ints coresponding to a pythagorean triplet
              that adds up to the target sum
    """
    for i in range(1, range_max, 2):
        for j in range(1, range_max, 2):
            triplet = euclid_pyth_triplet(i, j)
            if triplet_sum(triplet, target_sum):
                return triplet


def main():
    triplet = find_triplet_with_sum(50, 1000)
    print(triplet)
    print(triplet[0] * triplet[1] * triplet[2])


if __name__ == "__main__":
    main()
