def optimized_fibonacci(n):
    """
    List iteration has greater scalability for finding fibonacci numbers.

    When compared to the recursive method, this method does not need to recalculate old values,
    sums them from
    :param x: nth fibonacci number
    :return: provides the nth fibonacci number
    """

    if n < 0:
        raise Exception('Number must be greater than or equal to zero')
    if n >= 0:
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[-1] + fib[-2])
        return fib[-1] + fib[-2]


print(optimized_fibonacci(100000))

class SummableSequence(object):
    def __init__(self, ):

