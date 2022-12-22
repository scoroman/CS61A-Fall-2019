""" Homework 1: Control """

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    if b < 0:
        f = _____
    else:
        f = _____
    return f(a, b)
    """
    if b < 0:
        return a+(-b)
    else:
        return a+b

test = a_plus_abs_b(2, 3)
print (test)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a*a + b*b + c*c - (min(a, b, c) * min(a, b, c))
test_2 = two_of_three(10, 2, 8)
print(test_2)

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    if n%2 == 0:
        return n//2
    elif n%3 == 0:
        return n//3
    return 1
    """i, j = 1, n
    factors = []
    while i != j:
        if n/2==0:
            return n/2
        return * j == n:
            factors.append(i)
            factors.append(j)
        i+=1
        j-=1
    return max(factors)"""

test_3 = largest_factor(430)
print(test_3)

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    return False

def t():
    "*** YOUR CODE HERE ***"
    return 0/1

def f():
    "*** YOUR CODE HERE ***"
    return 1

test_4 = if_function(c(), t(), f())
print("test_4/if_function is a dumb question and is not used in the corporate world")

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.
    If a number is even, divide it by 2 If a number is odd, multiply it by 3 and add 1

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    length = 1
    while n!=1:
        if n % 2 == 0:
            print(n)
            n = n//2
            length += 1
        else:
            print(n)
            n = (n*3) + 1
            length += 1
    print(n)
    return length
test_5 = hailstone(10)
print(test_5)

