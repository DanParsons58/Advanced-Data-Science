import math


def f(x):
    if x <= 1:
        return x
    else:
        return f(x - 1) + f(x - 2)





def optimized_fibonacci(n):
    """
    Utilizes Binet's formula to calculate the nth fibonacci number.

    Optimizes for memory and time complexity by avoiding recursion.
    :param x: nth fibonacci number
    :return: provides the nth fibonacci number
    """

    return int((1 / (2 ** n * math.sqrt(5))) * ((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n))


print(optimized_fibonacci(1))
