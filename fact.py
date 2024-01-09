def fact(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n*fact(n-1)

def sum_series(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return n + sum_series(n-1)
