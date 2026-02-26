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
multiplied_numbers = list(map(lambda x, y: x * y, num1, num2))
print(multiplied_numbers)
str_numbers = ['1', '2', '3']
int_numbers = list(map(int, str_numbers))
print(int_numbers)
word= ['hello', 'world']
upper_words = list(map(str.upper, word))
print(upper_words)
lower_words = list(map(str.lower, upper_words))
print(lower_words)
print(type(squared_numbers))
print(type(upper_words))
def get_name_length(name):
    return len(name)
names = ['Alice', 'Bob', 'Charlie']
name_lengths = list(map(get_name_length, names))
print(name_lengths)
name_lengths_lambda = list(map(lambda name: len(name), names))
print(name_lengths_lambda)