# Converting from Decimal

# 3306@10 to @8:
# 3306/8 = 413 R2
# 413/8 = 51 R5
# 51/8 = 6 R3
# 6/8 = 0 R6
# 3306@10 = 6352@8 (Based on Remainders)

# n = number to convert
# b = base to convert to


def fromDecimal(n, b):
  ans = ''

  while (n >= b):
    ans = str(int(n % b)) + ans
    n = (n - (n % b)) / b

  ans = str(int(n % b)) + ans
  return ans


print(fromDecimal(3306, 8))
