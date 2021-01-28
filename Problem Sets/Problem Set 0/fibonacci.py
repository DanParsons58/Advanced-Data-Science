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
        for i in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])
        return fib[-1] + fib[-2]


print(optimized_fibonacci(1))


class SummableSequence(object):
    """
    Generates a class that sums sequence with initial list of num previous numbers.

    Accepts an initial list (initial) and appends a new value equal to the sum of previous
    num values until the number of iterations is met output
    num = the number of prior values that are summed to calculate the next value
    initial = the initial list
    output = the number in the list that is returned
    """

    def __init__(self, initial_string):
        self.initial_string = initial_string


    def __call__(self, output):
        if (self.output < 0) or (type(self.initial_string) != list):
            raise Exception('Improper parameter entry')
        if self.output <= len(self.initial):
            return self.initial[self.output-1]
        if self.output > len(self.initial):
            for l in range(self.output - len(self.initial)):
                sum = 0
                for i in range(self.num):
                    if (-i-1) < -len(self.initial):
                        break
                    sum += self.initial[-i-1]
                self.initial.append(sum)
            return self.initial[-1]


if __name__ == '__main__':
    new_seq = SummableSequence(3, [5, 7, 11], 5)
    print(new_seq(3, [5, 7, 11], 5))
