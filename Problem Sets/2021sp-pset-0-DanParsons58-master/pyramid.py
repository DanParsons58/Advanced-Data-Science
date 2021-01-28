#!/usr/bin/env python3
"""Print a pyramid to the terminal

A pyramid of height 3 would look like:

--=--
-===-
=====

"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter


def print_pyramid(rows):
    """
    Print a pyramid of a given height.

    :param int rows: total height of the pyramid
    """
    if rows <= 0:
        raise Exception('Number must be greater than or equal to zero')
    if rows >= 1:
        m = rows-1
        for n in range(rows):
            print("-" * (m - n) + "=" * (2 * n + 1) + "-" * (m - n))

if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=10, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(args.rows)
