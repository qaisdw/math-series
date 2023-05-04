from series.series import fibonacci,lucas,sum_series


def test_fibonacci():
    actual= fibonacci(0)
    expected = 0
    assert actual == expected

    actual= fibonacci(1)
    expected = 1
    assert actual == expected

    actual= fibonacci(2)
    expected = 1
    assert actual == expected

    actual= fibonacci(3)
    expected = 2
    assert actual == expected

    actual= fibonacci(4)
    expected = 3
    assert actual == expected

    actual= fibonacci(5)
    expected = 5
    assert actual == expected

    actual= fibonacci(10)
    expected = 55
    assert actual == expected


def test_lucas():
    
    assert lucas(0) == 2
    assert lucas(1) == 1  
    assert lucas(2) == 3
    assert lucas(3) == 4 
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(10) == 123


def test_sum_series():
    # Test the Fibonacci series
    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(2) == 1
    assert sum_series(3) == 2
    assert sum_series(4) == 3
    assert sum_series(5) == 5
    assert sum_series(10) == 55

    # Test the Lucas numbers
    assert sum_series(0, 2, 1) == 2
    assert sum_series(1, 2, 1) == 1
    assert sum_series(2, 2, 1) == 3
    assert sum_series(3, 2, 1) == 4
    assert sum_series(4, 2, 1) == 7
    assert sum_series(5, 2, 1) == 11
    assert sum_series(10, 2, 1) == 123

    # Test a custom series
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19
    assert sum_series(10, 3, 2) == 212
