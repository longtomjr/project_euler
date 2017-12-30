#!/usr/bin/env python3
# ^ Called a shabang -> easier to execute on Unix style OSes


def multiples(factor_list: list, maximum: int):
    """
    Returns a list of the multiples of the given factors

    :param factor_list: A 'list' of the factors to get the multiples of
    :param maximum: The maximum number that is used to look for multiples

    :returns: Returns a 'list' of the multiples of the given factors
    """

    # Creates an empty list to later append to
    multiples_list = []

    # Loops over all the factors in the list
    for factor in factor_list:
        # loops over all the numbers from 1 to the maximum
        for i in range(1, maximum):
            # Checks if the factor can be divided "cleanly" and add it to the
            # list if it can.
            if i % factor == 0:
                multiples_list.append(i)
            # Continues if not a multiple (continues with the loop)
            else:
                continue

    # 'multiples_list' changed to a 'set' (removes duplicates) and back to a
    # list
    # Read here: https://docs.python.org/3/library/stdtypes.html#types-set

    # Set is a collection like 'list', but unordered and can only have unique
    # entries therefore no duplicate entries. Very handy to remove duplicates
    return list(set(multiples_list))


def sum(l: list) -> int:
    """
    Gets the sum of all the entries in the given list
    """
    s = 0
    for i in l:
        s += i
    return s


def main():
    # print(multiples([3, 5], 1000))
    print(sum(multiples([3, 5], 1000)))


# "boilerplate" script to make sure python file is seen as a standalone
# executable. No need for you to use it.

if __name__ == "__main__":
    main()
