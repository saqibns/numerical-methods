__author__ = 'Saqib'
"""
Taylor's approximations for various functions. The approximations are done about the point x = 0.
"""
import math


def sinr(x, degree):
    """
    Calculates the sine of the angle 'x'.
    :param x: The angle in radian of whose sine is to be calculated.
    :param degree: The degree of the polynomial to which sine is to be approximated.
    :return: sine
    """
    num = x
    den = 1
    count = 1
    s = num / den
    deg = 1
    while deg <= degree:
        num = -num * x * x
        den = den * (count + 1) * (count + 2)
        count += 2
        s += (num / den)
        deg += 2
    return s


def sind(x, degree):
    """
    Calculate the sine of angle 'x'.
    :param x: The angle in degrees.
    :param degree: The degree to which the polynomial is to be approximated.
    :return: The value of sine of the angle 'x'.
    """
    rad = x * math.pi / 180
    return sinr(rad, degree)


def cosr(x, degree):
    """
    Calculate the cosine of angle 'x'.
    :param x: The angle in radian.
    :param degree: The degree of the polynomial up to which cosine is to be approximated.
    :return: The value of cosine of 'x'.
    """
    summation = 1.0
    deg = 2
    num = den = 1.0
    while deg <= degree:
        num *= -(x * x)
        den *= (deg - 1) * deg
        deg += 2
        summation += (num / den)
    return summation


def cosd(x, degree):
    rad = x * math.pi / 180
    return cosr(rad, degree)


def ln(x, degree):
    """
    Calculates the value of natural logarithm.
    :param x: The value at which ln is to be evaluated.
    :param degree: The degree of the polynomial to approximate ln x.
    :return: ln x
    """
    summation = 0.0
    deg = 1
    while deg <= degree:
        summation += ((x - 1.0) / (x + 1.0)) ** deg / deg
        deg += 2
    return 2 * summation


def e(x, degree):
    """
    Calculates the value of e ^ x using Maclaurin Series.
    :param x: The value at which e ^ x is to be calculated.
    :param degree: The degree up to which the polynomial is to be evaluated.
    :return: e ^ x
    """
    ex = 1
    count = 0
    num = den = 1.0
    while count <= degree:
        count += 1
        num *= x
        den *= count
        ex += (num / den)
    return ex


def sinh(x, degree):
    """
    Calculates the value of hyperbolic sine of 'x'.
    :param x: The value at which hyperbolic sine of 'x'.
    :param degree: The degree of the polynomial up to which sinh is to be approximated.
    :return: Hyperbolic sine of 'x'.
    """
    summation = x
    deg = 1
    num = x
    den = 1.0
    while deg <= degree:
        num *= (x * x)
        den *= (deg + 1) * (deg + 2)
        deg += 2
        summation += (num / den)
    return summation


def cosh(x, degree):
    """
    Calculates the value of hyperbolic cosine of 'x'.
    :param x: The value at which hyperbolic cosine of 'x'.
    :param degree: The degree of the polynomial up to which cosh is to be approximated.
    :return: Hyperbolic cosine of 'x'.
    """
    summation = num = den = 1.0
    deg = 0
    while deg <= degree:
        num *= (x * x)
        den *= (deg + 1) * (deg + 2)
        deg += 2
        summation += (num / den)
    return summation


def arcsin(x, degree):
    """
    Calculates the value of inverse of sine of 'x'.
    :param x: The value whose inverse sine is to be calculated.
    :param degree: The degree of the polynomial up to which the function is to be approximated.
    :return: The value of inverse of sine of 'x' in radian.
    """
    summation = x
    deg = 1
    term = x
    while deg <= degree:
        term *= (x * x)
        term *= deg
        term *= (deg / (deg + 1.0))
        deg += 2
        term /= deg
        summation += term
    return summation


# Tests
# print sinr(math.pi/4, 9)
# print sind(45.0, 9)
# print e(1, 10)
# print ln(5.0, 30)
# print cosr(1, 30)
# print sinh(2.0, 20)
# print cosh(2.0, 20)
# print arcsin(0.5, 20)
# print arcsin(0.75, 20)