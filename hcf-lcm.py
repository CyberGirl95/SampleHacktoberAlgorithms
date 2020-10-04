def hcf(x, y):
    """
    >>> hcf(24, 60)
    12
    >>> hcf(-12, 18)
    6
    >>> hcf(0, 24)
    1
    >>> hcf(a, 10) 
    Traceback (most recent call last):
      ...
    NameError: name 'a' is not defined
    """
    if x < y:
        smaller = abs(x)
        larger = abs(y)
    else:
        smaller = abs(y)
        larger = abs(x)
    hcf = 1  # Incase no common factor.
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


def lcm(x, y):
    """
    >>> lcm(24, 60)
    120
    >>> lcm(-12, 18)
    36
    >>> lcm(0, 24)
    0
    >>> lcm(a, 10) 
    Traceback (most recent call last):
      ...
    NameError: name 'a' is not defined
    """
    lcm = (abs(x) * abs(y)) // hcf(x, y)
    return lcm


if __name__ == "__main__":
    import doctest

    doctest.testmod()
