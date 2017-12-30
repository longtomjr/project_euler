#!/bin/bash/env python3

import csv


def get_grid():
    """
    Gets the grid of the csv as a two dimensional array
    """
    grid = []
    grid_str = []
    with open('problem_011_grid.csv') as f:
        grid_reader = csv.reader(f, delimiter=" ", quoting=csv.QUOTE_NONE)
        for row in grid_reader:
            for n in row:
                n = int(n)
            grid_str.append(row)

    # Changes the type of the entries in the nested array to int
    for row in grid_str:
        grid.append([int(x) for x in row])

    return grid


def get_right_product(grid, x, y, n):
    product = 1
    for i in range(n):
        product = product * grid[x][y + i]
    return product


def get_down_product(grid, x, y, n):
    product = 1
    for i in range(n):
        product = product * grid[x + i][y]
    return product


def get_diagonal_right_product(grid, x, y, n):
    product = 1
    for i in range(n):
        product = product * grid[x + i][y + i]
    return product


def get_diagonal_left_product(grid, x, y, n):
    product = 1
    for i in range(n):
        product = product * grid[x + i][y - i]
    return product


def get_products(grid, x, y, n):
    products = [
        get_right_product(grid, x, y, n),
        get_down_product(grid, x, y, n),
        get_diagonal_right_product(grid, x, y, n),
        get_diagonal_left_product(grid, x, y, n)
    ]
    return products

def get_biggest_product(grid, n):
    products = []
    for idx_x, val in enumerate(grid):
        for idx_y, val_y in enumerate(val):
            try:
                products.append(max(get_products(grid, idx_x, idx_y, n)))
            except IndexError:
                continue

    return max(products)

def main():
    print(get_biggest_product(get_grid(), 4))
    return 0


if __name__ == "__main__":
    main()
