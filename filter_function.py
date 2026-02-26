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
odd_numbers_lambda = list(filter(lambda n_: n_ % 2 != 0, numbers))
print(odd_numbers_lambda)
def greater_than_three(n):
    return n > 3
greater_than_three_numbers = list(filter(greater_than_three, numbers))
print(greater_than_three_numbers)
greater_than_three_numbers_lambda = list(filter(lambda n: n > 3, numbers))
print(greater_than_three_numbers_lambda)
def starts_with_a(s):
    return s.startswith('a')

