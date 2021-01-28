def print_pyramid(n):
    """Generates a pyramid of size n.

    Creates a pyramid of = symbols surrounded by - of length
    such that the pyramid is inside a box
    """
    if n <= 0:
        raise Exception('Number must be greater than or equal to zero')
    if n >= 1:
        m = n - 1
        for n in range(n):
            print("-" * (m - n) + "=" * (2 * n + 1) + "-" * (m - n))

print_pyramid(10)
