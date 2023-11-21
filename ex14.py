import itertools

def sum_variable_length_tuple(*args):
    return sum(itertools.chain.from_iterable(args))
print(sum_variable_length_tuple((1, 2, 3))) 