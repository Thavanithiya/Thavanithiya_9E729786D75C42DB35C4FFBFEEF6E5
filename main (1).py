def fact(n):
  """this is a recursive function to find factorial of an integer"""
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact(n - 1)

number = 5
res = fact(number)
print (" the factorial of {} is {}.". format(number, res))
