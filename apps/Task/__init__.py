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

def check_kwargs(**kwargs):
 for key, value in kwargs.items():
  print(f'{key} = {value}')
check_kwargs(name='lokesh', age=21, city='KTM')