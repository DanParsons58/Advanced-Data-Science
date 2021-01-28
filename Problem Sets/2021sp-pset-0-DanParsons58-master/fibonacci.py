#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """
    new_str = str(some_int)
    short_str = new_str[-9:-1]
    new_int = int(short_str)
    return new_int


def optimized_fibonacci(f):
    """
    List iteration has greater scalability for returning fibonacci numbers

    When compared to the recursive method, this method does not need to recalculate old values
    :param f: int nth fibonacci number
    :return: provides the nth fibonacci number
    """
    if f < 0:
        raise Exception('f must be greater or equal to 0')
    if f >= 0:
        fib = [0, 1]
        for i in range (2, f+1):
            fib.append(fib[-1] + fib[-2])
        return fib[-1] + fib[-2]

class SummableSequence(object):
    def __init__(self, num, initial, output ):
        self.num = num
        self.initial = initial
        self.output = output

    def __call__(self):
        if (self.output < 0) or (self.num < 0) or (type(self.initial) != list):
            raise Exception('improper parameter entry')
        if self.output <= len(self.initial):
            return self.initial[self.output-1]
        if self.output >len(self.initial):
            for length in range(self.output - len(self.initial)):
                sum = 0
                for i in range(self.num):
                    if (-i-1 <-len(self.initial)):
                        break
                    sum += self.initial[-i-1]
                self.initial.append(sum)
            return self.initial[-1]


if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
