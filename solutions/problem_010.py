#!/usr/bin/env python3

# import can be used to import any python file in the same folder
# the 'as' statemet can be used to import any module with
# a different name
import problem_007 as prime


def main():
    print(sum(prime.sieve_eratosthenes(2000000)) - 1)
    return 0


if __name__ == "__main__":
    main()
