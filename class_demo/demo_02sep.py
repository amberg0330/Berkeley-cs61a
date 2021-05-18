## Fibonacci sequence:
## 0, 1, 1, 2, 3, 5, 8, 13, 21， 34 ...
def fab_seq(n):
    """this function is to figure out the Nth Fabonacci sequence number.

    >>> fab_seq(3)
    1
    >>> fab_seq(10)
    34
    >>> fab_seq(2)
    1
    """
    prem, curr = 0, 1
    k = 2
    while k <= n:
      k += 1
      prem, curr = curr, curr + prem

    return prem

""" Generalizing.
>>> area_square(2)
4
"""
from math import pi, sqrt

def area(r, shape_constant):
    assert r > 0
    return r * r * shape_constant

def area_square(r):
    #return r * r
    return area(r, 1) # r must be > 0

def area_circle(r):
    # return r * r * pi
    return area(r, pi)

def area_hexagon(r):
    #return r * r * 3 * sqrt(3) / 2
    return area(r, 3 * sqrt(3) / 2 )



######################This is Generalizing quesiton2################
## method1 ##
def sum_naturals(n):
   """Generalizing - q2.
   >>> sum_naturals(5)
   15
   """
   total, k = 0, 1
   while k <= n:
      total, k = total + k, k + 1
   return total

#from math import pow
def sum_cubes(n):
    """Sum the first n cubes of natural numbers.
    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total

##for simplify###
def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first n terms of a sequence.
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_naturals(n):
    """Generalizing - q2.
    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)

def sum_cubes(n):
    """Sum the first n cubes of natural numbers.
    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)

##############how to calculate pi v4- 6##############
##lambda function##
from operator import mul
def pi_term(k):
    return 8 / mul(4 * k -3, 4 * k -1)

# summation(1000, pi_term) # this returns a nubmer very close to pi

##locally defined functions
def make_adder(n):
    """Return a funciton that takes one argumetn k and returns k + n.
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder


###lambda function###

## return statement
def end(n, d):
    """print the final digits of n in reverse order until D is found.
    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            return None

##
def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def search2(f):
    x = 0
    while not f(x):
        x += 1
    return x

def is_three(x):
    return x == 3

def square(x):
    return x * x

def positive(x):
    return max(0, square(x) - 100)

## inverse function
def inverse(f):
    """Return g(y) such that g(f(x))->x.
    >>> sqrt = inverse(square)
    >>> sqrt(16)
    4.0
    """
    return lambda y: search(lambda: f(x) == y)

## control function
from math import sqrt

def real_sqrt(x):
    if x > 0:
        return sqrt(x)
    else:
        return 0

def if_(c, t, f):
    if c:
        return t
    else:
        return f

def real_sqrt2(x):
    return if_(x > 0, sqrt(x), 0.0)
