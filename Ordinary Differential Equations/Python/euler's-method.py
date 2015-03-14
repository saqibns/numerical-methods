"""
The program used Euler's approximation in order to compute a numerical solution
to Ordinary Differential Equations in two variables.
"""
def euler(f, x0, y0, h, xn):
    """
    Euler's approximation in order to numerically compute the solution of an
    ordinary differential equation, whose function is 'f'.
    """
    print x0, y0
    x = x0
    while x < xn:
        y = y0 + h * f(x0, y0)
        x = x0 + h
        print x, y
        x0 = x
        y0 = y

def f(x, y):
    return (y - x) / (y + x)

def g(x, y):
    return 1 - y

#Tests
euler(f, 0.0, 1.0, 0.02, 0.1)
print 30 * '-'

euler(g, 0, 0, 0.1, 0.3)
print 30 * '-'
