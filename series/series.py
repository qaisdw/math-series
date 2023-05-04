

def fibonacci(n):
    """
    This function returns the nth value in the Fibonacci series.

    :param n: The position of the value to be returned.
    :return: The nth value in the Fibonacci series.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    This function returns the nth value in the Lucas numbers.

    :param n: The position of the value to be returned.
    :return: The nth value in the Lucas numbers.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
    

def sum_series(n, x=0, y=1):
    """
    This function returns the nth value in a series of numbers.

    :param n: The position of the value to be returned.
    :return: The nth value in the series.
    """
    a, b = x, y
    for i in range(n):
        a, b = b, a + b
    return a
