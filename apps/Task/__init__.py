# def outer_func(x):
#  def inner_func(y):
#   return x - y
#  return inner_func
# result = outer_func(15)
# print(result(5))

# def make_multiply(x):
#  def multiply(factor):
#   return x * factor
#  return multiply
# result = make_multiply(2)
# check = result(10)
# print(check)

# def make_divide(x):
#  def divide(div):
#   return x / div
#  return divide
# check_divide = make_divide(15)
# print(check_divide(5))

# def example(*args):
#  return sum(args)
# smth = example(1,2,3,4)
# print(smth)


# def kwars(**kwargs):
#  print(kwargs)

# kwars(a=1, b=2, c=3)

# def check_kwargs(**kwargs):
#  for key, value in kwargs.items():
#   print(f'{key} = {value}')
# check_kwargs(name='lokesh', age=21, city='KTM')

# def check_both(*args, **kwargs):
#  print(f'Args: {args}')
#  print(f'kwargs: {kwargs}')

# check_both(1,2,3, a=5, b=6, c=7)

# ''' Using Decorator in python '''

# def logger(func):
#  def wrapper(*args, **kwargs):
#   print(f'Expecting {func.__name__} with arguments of {args} and {kwargs}')
#  return wrapper

# @logger
# def add(x, y, **kwargs):
#  return x + y

# (add(5, 3, check=True, works=False, final='Kidding it works'))

# '''using Decoretor in python'''

#  def lower_func(*args, **kwargs):
#   print(f"Executing {func.__name__} and expect the result of args {args} and kwargs {kwargs}")
#   result = func(*args, **kwargs)
#   print(f"We are expecting the result of {result}")
#   return result
#  return lower_func

# @upper_func
# def add(x,y):
#  return x + y
# print(add(5,4))

# smth =  [
 
#   (2+3) * 4,x
#  (2+
# ]
# print(smth)

# def higherfuntion(numbers):
#  def lowerfunc(xparam):
#   return xparam - numbers
#  return lowerfunc

# double = higherfuntion(2)
# trible = higherfuntion(3)

# print(double(3))
# print(trible(3))

# def process_large_args(*args):
#     print(f"Processing {len(args)} arguments")
#     # Example operation: Sum all arguments
#     total_sum = sum(args)
#     print(f"Total sum: {total_sum}")

# # Creating the large list of arguments
# process_large_args(list(range(100000)))

# import os
# print(os.listdir("."))

numb