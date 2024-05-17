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

''' Using Decorator in python '''

def logger(func):
 def wrapper(*args, **kwargs):
  print(f'Expecting {func.__name__} with arguments of {args} and {kwargs}')
  result = func(*args, **kwargs)
  print(f'Expecting the  {func.__name__} returns result of {result}')
  return result
 return wrapper

@logger
def add(x, y, **kwargs):
 return x + y 

(add(5, 3, check=True, works=False, final='Kidding it works'))