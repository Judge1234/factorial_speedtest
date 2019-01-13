def cython_factorial(n):
    if n < 1:
        return 1
    else:
        return n * cython_factorial(n -1)
