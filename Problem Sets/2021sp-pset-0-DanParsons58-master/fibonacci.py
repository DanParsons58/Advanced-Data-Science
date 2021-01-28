#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int.

    :param int some_int: the number
    :rtype: int
    """
    new_str = str(some_int)
    short_str = new_str[-8:]
    new_int = int(short_str)
    return new_int


def optimized_fibonacci(f):
    """
    List iteration has greater scalability for returning fibonacci numbers.

    When compared to the recursive method, this method does not need to recalculate old values
    :param f: int nth fibonacci number
    :return: provides the nth fibonacci number
    """
    if f < 0:
        raise Exception('f must be greater or equal to 0')
    if f == 0:
        return 0
    if f >= 1:
        fib = [0, 1]
        for i in range(2, f + 1):
            fib.append(fib[-1] + fib[-2])
        return fib[-1]


class SummableSequence(object):
    """
    Generates a class that sums sequence with initial list of num previous numbers.

    Accepts an initial list (initial) and appends a new value equal to the sum of previous
    num values until the number of iterations is met output
    :num: the number of prior values that are summed to calculate the next value
    :initial: the initial list
    :output: the number in the list that is returned

    """
    def __init__(self, num, initial):
        self.num = num
        self.initial = initial

    def __call__(self, output):
        self.output = output
        if (self.output < 0) or (self.num < 0) or (type(self.initial) != list):
            raise Exception('improper parameter entry')
        if self.output <= len(self.initial):
            return self.initial[self.output]
        if self.output > len(self.initial):
            for length in range(self.output - len(self.initial)):
                sum = 0
                for i in range(self.num):
                    if len(self.initial) < length:
                        break
                    sum += self.initial[-i - 1]
                self.initial.append(sum)
            return self.initial[-1]


if __name__ == "__main__":
    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(3, [5, 7, 11])
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
