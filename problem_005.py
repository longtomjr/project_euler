#!/usr/bin/env python3

# NOTE: range_floor is an optional parameter that has a default of 1
def even_divisible_min(range_ceiling: int, range_floor=1) -> int:
    """
    Gets the smallest number that is evenly divisible by all the
    numbers in the range specified

    :param range_ceiling: The upper limit of the range of numbers to
                          be divided by
    :param range_floor: The smallest number of the range (where it
                        should start)
    :returns: The minimum evenly divisible number by the whole range
    """
    n = 1
    # infinite loop to re-run the 'for' loop everytime a number
    # is not valid
    while True:
        for i in range(range_floor, range_ceiling + 1):
            # Checks if 'n' is not evenly divisible by 'i'
            # If so n is changed to be one larger and the for loop
            # is exited so it can start again with the new number
            if n % i != 0:
                n = n + 1
                break
            # Checks if i is the upper limit and finishes the
            # function if it is.
            elif i == range_ceiling:
                return n
            else:
                continue


def main():
    print(even_divisible_min(20))


if __name__ == "__main__":
    main()
