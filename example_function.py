from find_fit_input import finder
import sys


def step(a, b):
    return {"a": a + 1, "b": b}

@finder(step=step)
def example_function(a, b):
    result = 0
    for i in range(a + 1):
        result += i ** i
    return result + b


sys.set_int_max_str_digits(1_000_000_000)

print(example_function(a=3, b=1))
