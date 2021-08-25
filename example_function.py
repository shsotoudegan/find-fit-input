from find_fit_input import finder

@finder
def example_function(a):
    result = 0
    for i in range(a + 1):
        result += i ** i
    return result

print(example_function(3))
