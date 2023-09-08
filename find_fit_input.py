"""this is a simple python3 project. In this project, we're find a input for function, which ganna makes functions proccess < t > minutes.
 To reach this goal, we use timeit module and decorator."""


from functools import wraps
from timeit import timeit


def finder(func=None, *, step, target=0.04, error=0.01, n=2):
    """A wrapper, find input, which in (target time - error, target time + error) interval"""
    def finder_decorator(func):
        @wraps(func)
        def wrapper(**kwargs):
            period = 0
            while not ((period <= (target + error)) and (period >= (target - error))):
                kwargs = step(**kwargs)
                period = timeit(stmt="function(**kwargs)", number=n, globals={'kwargs': kwargs, 'function': func})/float(n)
                if period > (target + error):
                    print("NOT EXIST!")
            else:
                print(f"function: {func.__name__},\ninput: {kwargs},\ntime: {period},\ntarget time: {target},\nerror: {error},\ndifference: {target - period}")
            return func(**kwargs)
        return wrapper
    
    if func is None:
        return finder_decorator
    else:
        return finder_decorator(func)