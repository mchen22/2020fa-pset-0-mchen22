#!/usr/bin/env python3
"""Print a pyramid to the terminal
A pyramid of height 3 would look like:
--=--
-===-
=====
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter


def print_pyramid(rows):
    """Print a pyramid of a given height
    :param int rows: total height
    """
    try:
        if rows == '1':
            return "="
        else:
            # number of "=" on the last row
            m = 2 * rows - 1


            # Outer loop for number of rows
            for n in range(rows):

                # Print next one when finish printing each row
                if (n != 0): s += "\n"
                else: s = ''

                # inner loop for generating number of "-" to the LHS
                for i in range(rows-n-1):
                    s += "-"

                # Inner loop for generating number of "="
                for j in range(2 * n + 1):
                    s += "="

                # inner loop for generating number of "-" to the RHS
                for i in range(rows-n-1):
                    s += "-"

            return print(s)
    except:
        raise NotImplementedError("Called with rows={}".format(rows))


if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=3, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(args.rows)