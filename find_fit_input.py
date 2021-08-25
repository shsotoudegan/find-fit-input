"""this is a simple python3 project. In this project, we're find a input for function, which ganna makes functions proccess < t > minutes.
 To reach this goal, we use timeit module and decorator."""


from functools import wraps
from timeit import timeit


def finder(func, target=0.04, error=0.01, n=2):
    """A wrapper, find input, which in (target time - error, target time + error) interval"""
    @wraps(func)
    def wrapper(a):
        period = 0
        inp = a
        a = -1
        while not ((period <= (target + error)) and (period >= (target - error))):
            a += 1
            period = timeit(stmt="function(a)", number=n, globals={'a': a, 'function': func})/float(n)
            if period > (target + error):
                print("NOT EXIST!")
        else:
            print(f"function: {func.__name__},\ninput: {a},\ntime: {period},\ntarget time: {target},\nerror: {error},\ndifference: {target - period}")
        return func(inp)
    return wrapper
