def even(n):
    return n % 2 == 0
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(even, numbers))
print(even_numbers)
even_numbers_lambda = list(filter(lambda n: n % 2 == 0, numbers))
print(even_numbers_lambda)
def odd(n_):
        return n_ % 2 != 0
odd_numbers = list(filter(odd, numbers))
print(odd_numbers)