#!/usr/bin/env python3

# Hierdie is pretty straight forward, figure dit self uit en kyk
# of jy dit kan improve

def sum_of_squares(n):
    x = 0
    for i in range(1, n+1):
        x = x + i ** 2
    return x


def square_of_sums(n):
    return sum(range(1, n+1)) ** 2


def main():
    print(square_of_sums(100) - sum_of_squares(100))


if __name__ == "__main__":
    main()
