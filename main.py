# Get the first N elements of a Generator in Python

from itertools import islice


def g():
    yield 1
    yield 2
    yield 3


gen = g()

first_2 = list(islice(gen, 2))
print(first_2)  # 👉️ [1, 2]