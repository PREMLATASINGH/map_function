def square(x):
    return x * x
print(square(5))  
print(square(-3))
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)
squared_numbers_lambda = list(map(lambda x: x * x, numbers))
print(squared_numbers_lambda)
cubed_numbers = list(map(lambda x: x ** 3, numbers))
print(cubed_numbers)
num1= [1, 2, 3]
num2= [4, 5, 6]
added_numbers = list(map(lambda x, y: x + y, num1, num2))
print(added_numbers)