# Recursion - a function that calls itself repeatedly, as opposed to a for/while loop


def factorial(x):
  if x == 1:
    return 1
  return x * factorial(x - 1)


print(factorial(10))

# Procedure:
# factorial(10) => 10 * factorial(9)
# factorial(9) => 9 * factorial(8)
# factorial(8) => 8 * factorial(7)
# factorial(7) => 7 * factorial(6)
# factorial(6) => 6 * factorial(5)
# factorial(5) => 5 * factorial(4)
# factorial(4) => 4 * factorial(3)
# factorial(3) => 3 * factorial(2)
# factorial(2) => 2 * factorial(1)
# factorial(1) => 1
#
# So, factorial(10) => 10 * (9 * (8 * (7 * (6 * (5 * (4 * (3 * (2 * (1))))))))) => 3628800
