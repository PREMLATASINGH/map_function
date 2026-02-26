def square(x):
    return x * x
print(square(5))  
print(square(-3))
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)
squared_numbers_lambda = list(map(lambda x: x * x, numbers))
print(squared_numbers_lambda)