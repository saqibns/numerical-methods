__author__ = 'Saqib'
"""
Various series to calculate the value of pi.
"""
import random
import math
def leibniz_gregory_madhava(terms):
    """
    Calculates the value of pi using Leibniz-Gregory-Madhava series.
    :param terms: The number of terms to be taken in the series
    :return: The value of pi
    """
    count = 1
    summation = 0.0
    while count <= terms:
        summation += (((-1) ** (count + 1)) / (2.0 * count - 1.0))
        count += 1
    return summation * 4.0


def euler(terms):
    """
    Calculates the value of pi using Euler's series.
    :param terms: The number of terms to be taken in the series.
    :return: The value of pi.
    """
    num = 2.0
    num_count = 2
    den = 3.0
    den_count = 3
    count = 1
    sum = 0.0
    while count <= terms:
        sum += (num / den)
        num_count += 1
        num *= num_count
        den_count += 2
        den *= den_count
        count += 1
    return sum * 2


def euler2(terms):
    """
    Calculates the value of pi using summation (1 / n_squared).
    :param terms: The number of terms to be taken in the series.
    :return: The value of pi.
    """
    def absolute(x):
        """
        Calculates the absolute value of a number.
        :param x: The value whose absolute is to be obtained.
        :return: The absolute value.
        """
        if x < 0:
            return -x
        return x


    def square_root(x, error = 0.001, iterations = 10):
        """
        Calculates the square root using Newton-Raphson method.
        :param x: The value whose square root is to be calculated.
        :param error: The margin of error acceptable.
        :param iterations: The number of iterations to be performed.
        :return: Square root of 'x'.
        """
        x0 = 1.0
        x1 = (x0 * x0 + x) / (2.0 * x0)
        i = 1
        while (absolute(x1 - x0) > error) and (i <= iterations):
            x0 = x1
            x1 = (x0 * x0 + x) / (2.0 * x0)
            i += 1
        return x1

    # Calculate the sum
    summation = 0.0
    count = 1
    while count <= terms:
        summation += (1 / float(count * count))
        count += 1
    return square_root(6 * summation, 0.0000001)


def monte_carlo(trials):
    """
    Calculates the value of pi using the Monte-Carlo method.
    :param trials: The number of trials to be performed.
    :return:
    """
    def is_inside_quadrant(x, y):
        if x * x + y * y < 1.0:
            return True
        else:
            return False
    inside = 0
    total = 0
    for i in xrange(trials):
        x = random.random()
        y = random.random()
        total += 1
        if is_inside_quadrant(x, y):
            inside += 1
    return 4.0 * inside / total


def ramanujan(terms):
    """
    Calculates the value of pi using Ramanujan's series.
    :param terms: The number of terms to be used in the summation.
    :return: The value of pi.
    """
    def absolute(x):
        """
        Calculates the absolute value of a number.
        :param x: The value whose absolute is to be obtained.
        :return: The absolute value.
        """
        if x < 0:
            return -x
        return x

    def square_root(x, error = 0.001, iterations = 10):
        """
        Calculates the square root using Newton-Raphson method.
        :param x: The value whose square root is to be calculated.
        :param error: The margin of error acceptable.
        :param iterations: The number of iterations to be performed.
        :return: Square root of 'x'.
        """
        x0 = 1.0
        x1 = (x0 * x0 + x) / (2.0 * x0)
        i = 1
        while (absolute(x1 - x0) > error) and (i <= iterations):
            x0 = x1
            x1 = (x0 * x0 + x) / (2.0 * x0)
            i += 1
        return x1

    def factorial(n):
        f = 1
        for j in xrange(1, n + 1):
            f *= j
        return f

    summation = 0.0
    for k in xrange(terms):
        summation += (factorial(4 * k) / (factorial(k) ** 4)) * ((26390.0 * k + 1103.0) / (396.0 ** (4.0 * k)))
    return 99 ** 2 / (2 * square_root(2, 0.00000000001)) / summation


# Tests
# print leibniz_gregory_madhava(1000)
# print euler(100)
# print euler2(10000)
# print monte_carlo(10000000)
print ramanujan(3)
print math.pi