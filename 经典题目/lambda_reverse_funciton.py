"""make reverse function using lumbda"""
# https://www.youtube.com/watch?v=QIh6CyrWhvw&list=PL6BsET-8jgYXeefqDPnwLJ03jyw5-KKTT&index=7&ab_channel=JohnDeNeroJohnDeNero

def search(f):
    x = 0 
    while True: 
        if f(x):
            return x 
        x +=1 


def is_three(x):
    x == 3 

def square(x):
    return x * x 

def positive(x):
    return (max(0, square(x) - 100))

def inverse(f):
    """Return g(y) such that g(f(x)) --> x. 
    >>> sqrt = inverse(square)
    >>> sqrt(16)
    4 
    """
    return lambda y: search(lambda x: f(x) == y)
